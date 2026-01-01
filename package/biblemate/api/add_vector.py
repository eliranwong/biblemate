import apsw, re, os, json
from agentmake.utils.rag import get_embeddings
from prompt_toolkit.shortcuts import ProgressBar
from biblemate import config, BIBLEMATEDATA


def add_vector_data(db_file="dictionary.db", table="Dictionary", h2=False):
    db_file = os.path.join(BIBLEMATEDATA, db_file)
    if os.path.isfile(db_file):
        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            # Check if 'entry' column already exists
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            if 'entry' not in column_names:
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry TEXT;")
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry_vector TEXT;")
            # Update 'entry' and 'entry_vector' columns
            cursor.execute(f"SELECT path, content FROM {table};")
            with ProgressBar() as pb:
                for path, content in pb(cursor.fetchall()):
                    search = re.search(f">([^<>]+?)</{'h2' if h2 else 'ref'}>", content)
                    if search:
                        entry = search.group(1)
                        vector = get_embeddings([entry], config.embedding_model)
                        vector_str = json.dumps(vector.tolist())
                        cursor.execute(f"UPDATE {table} SET entry = ?, entry_vector = ? WHERE path = ?;", (entry, vector_str, path))
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN content;")
            #cursor.execute(f"VACUUM;")

def add_vector_names(create_table=True):
    from uniquebible.util.HBN import HBN
    db_file = os.path.join(BIBLEMATEDATA, "exlb.db")
    table = "exlbn"
    if os.path.isfile(db_file):
        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            if create_table:
                cursor.execute(f"""
CREATE TABLE IF NOT EXISTS {table} (
    path          TEXT NOT NULL UNIQUE,
    entry         TEXT,
    entry_vector  TEXT
)
""")
            # Update 'entry' and 'entry_vector' columns
            with ProgressBar() as pb:
                for path, entry in pb(HBN.entries.items()):
                    entry = re.sub("<[^<>]*?>", "", entry).strip()
                    vector = get_embeddings([entry], config.embedding_model)
                    vector_str = json.dumps(vector.tolist())
                    cursor.execute(f"INSERT OR IGNORE INTO {table} (path, entry, entry_vector) VALUES (?,?,?)", (path, entry, vector_str))
            #cursor.execute(f"VACUUM;")

def fix_vector_collections(db_file="collection.db", table="PARALLEL"):
    db_file = os.path.join(BIBLEMATEDATA, db_file)
    if os.path.isfile(db_file):
        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            # Update 'entry' and 'entry_vector' columns
            cursor.execute(f"SELECT path, entry FROM {table} WHERE entry LIKE ':%';")
            with ProgressBar() as pb:
                for path, entry in pb(cursor.fetchall()):
                    entry = re.sub("^:", "", entry).strip()
                    vector = get_embeddings([entry], config.embedding_model)
                    vector_str = json.dumps(vector.tolist())
                    cursor.execute(f"UPDATE {table} SET entry = ?, entry_vector = ? WHERE path = ?;", (entry, vector_str, path))
            #cursor.execute(f"VACUUM;")

def add_vector_collections(db_file="collection.db", table="PROMISES", h2=False):
    db_file = os.path.join(BIBLEMATEDATA, db_file)
    if os.path.isfile(db_file):
        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            # Check if 'entry' column already exists
            cursor.execute(f"PRAGMA table_info({table});")
            columns = cursor.fetchall()
            column_names = [col[1] for col in columns]
            if 'entry' not in column_names:
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN path TEXT;")
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry TEXT;")
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry_vector TEXT;")
            # Update 'entry' and 'entry_vector' columns
            cursor.execute(f"SELECT Tool, Number, Topic FROM {table};")
            with ProgressBar() as pb:
                for tool, number, topic in pb(cursor.fetchall()):
                    path = f"{tool}.{number}"
                    entry = re.sub(r"^[\.0-9: ]+?([^\.0-9 ])", r"\1", topic).strip()
                    vector = get_embeddings([entry], config.embedding_model)
                    vector_str = json.dumps(vector.tolist())
                    cursor.execute(f"UPDATE {table} SET path = ?, entry = ?, entry_vector = ? WHERE Tool = ? AND Number = ?;", (path, entry, vector_str, tool, number))
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN Tool;")
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN Number;")
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN Topic;")
            cursor.execute(f"ALTER TABLE {table} DROP COLUMN Passages;")
            #cursor.execute(f"VACUUM;")

def add_vector_encyclopedias():
    db_file = os.path.join(BIBLEMATEDATA, "encyclopedia.db")
    if os.path.isfile(db_file):
        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            for table in ("DAC", "DCG", "HAS", "ISB", "KIT", "MSC"):
                print(f"Working on table `{table}` ...")
                # Check if 'entry' column already exists
                cursor.execute(f"PRAGMA table_info({table});")
                columns = cursor.fetchall()
                column_names = [col[1] for col in columns]
                if 'entry' not in column_names:
                    cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry TEXT;")
                    cursor.execute(f"ALTER TABLE {table} ADD COLUMN entry_vector TEXT;")
                # Update 'entry' and 'entry_vector' columns
                cursor.execute(f"SELECT path, content FROM {table};")
                with ProgressBar() as pb:
                    for path, content in pb(cursor.fetchall()):
                        search = re.search(">([^<>]+?)</ref>", content)
                        if search:
                            entry = search.group(1)
                            vector = get_embeddings([entry], config.embedding_model)
                            vector_str = json.dumps(vector.tolist())
                            cursor.execute(f"UPDATE {table} SET entry = ?, entry_vector = ? WHERE path = ?;", (entry, vector_str, path))
                cursor.execute(f"ALTER TABLE {table} DROP COLUMN content;")
            #cursor.execute(f"VACUUM;")