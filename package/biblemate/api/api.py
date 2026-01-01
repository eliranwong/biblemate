from agentmake import agentmake
from agentmake.utils.online import get_local_ip
from agentmake.plugins.uba.lib.BibleParser import BibleVerseParser
from biblemate import config, AGENTMAKE_CONFIG
from urllib.parse import quote
import requests, os, re, traceback

DEFAULT_MODULES = {
    "bible": config.default_bible,
    "chapter": config.default_bible,
    "xref": config.default_bible,
    "treasury": config.default_bible,
    "search": config.default_bible,
    "genesis": config.default_bible,
    "exodus": config.default_bible,
    "leviticus": config.default_bible,
    "numbers": config.default_bible,
    "deuteronomy": config.default_bible,
    "joshua": config.default_bible,
    "judges": config.default_bible,
    "ruth": config.default_bible,
    "samuel1": config.default_bible,
    "samuel2": config.default_bible,
    "kings1": config.default_bible,
    "kings2": config.default_bible,
    "chronicles1": config.default_bible,
    "chronicles2": config.default_bible,
    "ezra": config.default_bible,
    "nehemiah": config.default_bible,
    "esther": config.default_bible,
    "job": config.default_bible,
    "psalms": config.default_bible,
    "proverbs": config.default_bible,
    "ecclesiastes": config.default_bible,
    "songs": config.default_bible,
    "isaiah": config.default_bible,
    "jeremiah": config.default_bible,
    "lamentations": config.default_bible,
    "ezekiel": config.default_bible,
    "daniel": config.default_bible,
    "hosea": config.default_bible,
    "joel": config.default_bible,
    "amos": config.default_bible,
    "obadiah": config.default_bible,
    "jonah": config.default_bible,
    "micah": config.default_bible,
    "nahum": config.default_bible,
    "habakkuk": config.default_bible,
    "zephaniah": config.default_bible,
    "haggai": config.default_bible,
    "zechariah": config.default_bible,
    "malachi": config.default_bible,
    "matthew": config.default_bible,
    "mark": config.default_bible,
    "luke": config.default_bible,
    "john": config.default_bible,
    "acts": config.default_bible,
    "romans": config.default_bible,
    "corinthians1": config.default_bible,
    "corinthians2": config.default_bible,
    "galatians": config.default_bible,
    "ephesians": config.default_bible,
    "philippians": config.default_bible,
    "colossians": config.default_bible,
    "thessalonians1": config.default_bible,
    "thessalonians2": config.default_bible,
    "timothy1": config.default_bible,
    "timothy2": config.default_bible,
    "titus": config.default_bible,
    "philemon": config.default_bible,
    "hebrews": config.default_bible,
    "james": config.default_bible,
    "peter1": config.default_bible,
    "peter2": config.default_bible,
    "john1": config.default_bible,
    "john2": config.default_bible,
    "john3": config.default_bible,
    "jude": config.default_bible,
    "revelation": config.default_bible,
    "parallel": config.default_bible,
    "promise": config.default_bible,
    "commentary": config.default_commentary,
    "encyclopedia": config.default_encyclopedia,
    "lexicon": config.default_lexicon,
}

# api
def run_bm_api(query: str, language: str="eng") -> str:
    # 1. Define the URL
    url = os.getenv("BM_API_ENDPOINT", "https://biblemate.gospelchurch.uk/api/data")
    # 2. Define your parameters
    payload = {
        "query": quote(query),
        "language": language, # Optional
        "token": os.getenv("BM_API_CUSTOM_KEY", "") # Optional
    }
    # 3. Send the GET request
    try:
        response = requests.get(url, params=payload, timeout=int(os.getenv("BM_API_TIMEOUT", 10)))
        # 4. Check if the request was successful (Status Code 200)
        if response.status_code == 200:
            data = response.json()  # Convert JSON response to Python dict
            api_content = data.get("content", "[NO_CONTENT]")
            if api_content == "\n\n":
                api_content = "[NO_CONTENT]"
            return api_content
        else:
            print(f"Error: {response.status_code}")
            return response.text
    except requests.exceptions.ConnectionError:
        print("Could not connect to BibleMate AI API server.")
    except Exception as err:
        traceback.print_exc()
        return f"An error occurred: {err}"
