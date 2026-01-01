import numpy as np
import sqlite3, apsw
import json, os, re
from agentmake import OllamaAI, OLLAMA_FOUND, OLLAMA_NOT_FOUND_MESSAGE, AGENTMAKE_USER_DIR, agentmake, getDictionaryOutput
from agentmake.utils.rag import get_embeddings, cosine_similarity_matrix
from prompt_toolkit.shortcuts import ProgressBar
from biblemate import config, BIBLEMATEDATA
from biblemate.api.api import run_bm_api
from agentmake.plugins.uba.lib.BibleBooks import BibleBooks
from agentmake.backends.ollama import OllamaAI

# local
def search_bible(request:str, book:int=0, module=config.default_bible, search_request=False) -> str:
    
    # extract the search string
    if search_request:
        search_string = request
    else:
        try:
            schema = {
                "name": "search_bible",
                "description": "search the bible; search string must be given",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "search_string": {
                            "type": "string",
                            "description": "search string for searching the bible",
                        },
                    },
                    "required": ["search_string"],
                },
            }
            search_string = getDictionaryOutput(request, schema=schema, backend=config.backend, model=config.model)["search_string"]
        except:
            search_string = agentmake(request, system="biblemate/identify_search_string")[-1].get("content", "").strip()
            search_string = re.sub(r"^.*?```(.+?)```.*?$", r"\1", search_string.replace("```search_string", ""), flags=re.DOTALL).replace("```", "").strip()
        search_string = re.sub('''^['"]*(.+?)['"]*$''', r"\1", search_string).strip()
    
    # perform the searches
    abbr = BibleBooks.abbrev["eng"]
    # exact matches
    exact_matches_content = run_bm_api(f"literal:::{abbr[str(book)][0]},{module}:::{search_string}" if book else f"literal:::{module}:::{search_string}")
    
    # semantic matches
    bible_file = os.path.join(BIBLEMATEDATA, "bible.db")
    if not OLLAMA_FOUND:
        semantic_matches = []
        semantic_matches_content = f"[{OLLAMA_NOT_FOUND_MESSAGE}]"
    elif os.path.isfile(bible_file):
        db = BibleVectorDatabase()
        semantic_matches = [f"{abbr[str(b)][0]} {c}:{v}" for b, c, v, _ in db.search_meaning(search_string, top_k=config.max_semantic_matches, book=book)]
        semantic_matches_content = run_bm_api(f"verses:::{module}:::"+";".join(semantic_matches)) if semantic_matches else ""
    else:
        print("Download the data file `bible.db` via the `.download` command to enable semantic search.")
        semantic_matches = []
        semantic_matches_content = ""
    
    output = f'''# Search for `{search_string}`

## Exact Matches

{exact_matches_content}

## Similar Matches [{len(semantic_matches)} verse(s)]

{semantic_matches_content}'''

    return output


class BibleVectorDatabase:
    """
    Sqlite Vector Database via `apsw`
    https://rogerbinns.github.io/apsw/pysqlite.html

    Requirement: Install `Ollama` separately

    ```usage
    from biblemate.api.bible import BibleVectorDatabase
    db = BibleVectorDatabase('my_bible.bible') # edit 'my_bible.bible' to your bible file path
    db.add_vectors() # add vectors to the database
    results = db.search_meaning("Jesus love", 10)
    ```
    """

    def __init__(self, uba_bible_path: str=None):
        if not uba_bible_path:
            uba_bible_path = os.path.join(BIBLEMATEDATA, "bible.db")
        # check if file exists
        if os.path.isfile(uba_bible_path):
            # Download embedding model
            OllamaAI.downloadModel(config.embedding_model) # requires installing Ollama
            # init
            self.conn = apsw.Connection(uba_bible_path)
            self.cursor = self.conn.cursor()
            self.cursor.execute("PRAGMA auto_vacuum = FULL;")
            self._create_table()

    def __del__(self):
        if not self.conn is None:
            self.conn.close()

    def clean_up(self):
        self.cursor.execute("VACUUM;")
        self.cursor.execute("PRAGMA auto_vacuum = FULL;")

    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS vectors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                book INTEGER,
                chapter INTEGER,
                verse INTEGER,
                text TEXT,
                vector TEXT
            )
        """
        )

    def getAllVerses(self):
        query = "SELECT * FROM Verses ORDER BY Book, Chapter, Verse"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def add_vectors(self):
        allVerses = self.getAllVerses()

        with ProgressBar() as pb:
            for book, chapter, verse, scripture in pb(allVerses):
                vector = get_embeddings([scripture], config.embedding_model)
                self.add_vector(book, chapter, verse, scripture, vector)
        self.clean_up()

    def add_vector(self, book, chapter, verse, text, vector):
        vector_str = json.dumps(vector.tolist())
        self.cursor.execute("SELECT COUNT(*) FROM vectors WHERE text = ?", (text,))
        if self.cursor.fetchone()[0] == 0:  # Ensure no duplication
            try:
                self.cursor.execute("INSERT INTO vectors (book, chapter, verse, text, vector) VALUES (?, ?, ?, ?, ?)", (book, chapter, verse, text, vector_str))
            except sqlite3.IntegrityError:
                pass  # Ignore duplicate entries

    def search_vector(self, query_vector, top_k=3, book=0):
        q = "SELECT text, vector FROM vectors"
        args = ()
        if book and isinstance(book, int):
            q += " WHERE book = ?"
            args = (book,)
        elif book and (isinstance(book, str) or isinstance(book, tuple)):
            q += f" WHERE book IN {book}"
        elif book and isinstance(book, list):
            q += f" WHERE book IN {tuple(book)}"
        self.cursor.execute(q, args)
        rows = self.cursor.fetchall()
        if not rows:
            return []
        
        texts, vectors = zip(*[(row[0], np.array(json.loads(row[1]))) for row in rows if row[0] and row[1]])
        document_matrix = np.vstack(vectors)
        
        similarities = cosine_similarity_matrix(query_vector, document_matrix)
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        return [texts[i] for i in top_indices]

    def search_meaning(self, query, top_k=3, book=0):
        queries = self.search_vector(get_embeddings([query], config.embedding_model)[0], top_k=top_k, book=book)
        return self.search_verses(queries)

    def search_verses(self, queries: list, book: int=0):
        allVerses = []
        for query in queries:
            allVerses += self.search_verse(query, book=book)
        return allVerses

    def search_verses_partial(self, queries: list, book: int=0):
        allVerses = []
        for query in queries:
            allVerses += self.search_verse(query, partial=True, book=book)
        return allVerses

    def search_verse(self, query: str, partial: bool=False, book: int=0):
        book_search = f"Book = {book} AND " if book else ""
        full_match = f'''SELECT * FROM Verses WHERE {book_search}Scripture = ? ORDER BY Book, Chapter, Verse'''
        partial_match = f'''SELECT * FROM Verses WHERE {book_search}Scripture LIKE ? ORDER BY Book, Chapter, Verse'''
        self.cursor.execute(partial_match if partial else full_match, (f"""%{query}%""" if partial else query,))
        return self.cursor.fetchall()