from biblemate import config
from biblemate.api.api import run_bm_api
from agentmake.utils.rag import get_embeddings, cosine_similarity_matrix
from typing import Union
import os, apsw, json
import numpy as np
import urllib.parse


class UBASearches:
    
    @staticmethod
    def search_data(db_file: str, sql_table: str, query: str, top_k: int=3, bible="") -> Union[list, str]:
        """search for a query"""
        if not os.path.isfile(db_file):
            return "Invalid database file."

        def get_exlb_keyword(sql_table):
            if sql_table == "exlbt":
                return "topics:::"
            elif sql_table == "exlbn":
                return "names:::"
            elif sql_table == "exlbp":
                return "characters:::"
            elif sql_table == "exlbl":
                return "locations:::"
            else:
                return ""

        query = urllib.parse.unquote(query).replace("「」", "/")

        keywords = {
            "dictionary.db": "dictionaries:::",
            "encyclopedia.db": f"encyclopedias:::{sql_table}:::",
            "exlb.db": get_exlb_keyword(sql_table),
            "collection.db": f"{'promises' if sql_table == 'PROMISES' else 'parallels'}:::{bible}:::",
        }

        with apsw.Connection(db_file) as connection:
            cursor = connection.cursor()
            # search for an exact match
            if "+" in query:
                cmd_prefix = keywords.get(os.path.basename(db_file))
                path, _ = query.split("+", 1)
                return run_bm_api(f"{cmd_prefix}{path}")
            else:
                cursor.execute(f"SELECT * FROM {sql_table} WHERE entry = ?;", (query,))
                rows = cursor.fetchall()
            if not rows: # perform similarity search if no an exact match
                # convert query to vector
                query_vector = get_embeddings([query], config.embedding_model)[0]
                # fetch all entries
                cursor.execute(f"SELECT entry, entry_vector FROM {sql_table}")
                all_rows = cursor.fetchall()
                if not all_rows:
                    return []
                # build a matrix
                entries, entry_vectors = zip(*[(row[0], np.array(json.loads(row[1]))) for row in all_rows if row[0] and row[1]])
                document_matrix = np.vstack(entry_vectors)
                # perform a similarity search
                similarities = cosine_similarity_matrix(query_vector, document_matrix)
                top_indices = np.argsort(similarities)[::-1][:top_k]
                # return top matches
                return [entries[i] for i in top_indices]
            elif len(rows) == 1: # single exact match
                cmd_prefix = keywords.get(os.path.basename(db_file))
                path = rows[0][0]
                content = run_bm_api(f"{cmd_prefix}{path}")
                if sql_table == "exlbl" and "Click HERE for a Live Google Map" in content:
                    cursor.execute(f"SELECT lat, lng FROM {sql_table}i WHERE path = ?;", (path,))
                    lat, lng = cursor.fetchone()
                    content = content.replace("Click HERE for a Live Google Map", f"https://maps.google.com/?q={lat},{lng}&ll={lat},{lng}&z=9")
                return content
            else:
                return [f"{path}+{entry}" for path, entry, _ in rows]