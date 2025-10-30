import os
from biblemate import config, BIBLEMATE_VERSION
from agentmake import AGENTMAKE_USER_DIR, readTextFile
import argparse

parser = argparse.ArgumentParser(description = f"""BibleMate AI MCP Server {BIBLEMATE_VERSION} CLI options""")
parser.add_argument("-b", "--backend", action="store", dest="backend", help="AI backend; overrides the default backend temporarily.")
parser.add_argument("-p", "--port", action="store", dest="port", help=f"specify a port for the MCP server to use, e.g. {config.mcp_port}; applicable to command `biblematemcp` only")
args = parser.parse_args()

if args.backend:
    config.backend = args.backend

def mcp():
    builtin_mcp_server = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bible_study_mcp.py")
    user_mcp_server = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "bible_study_mcp.py") # The user path has the same basename as the built-in one; users may copy the built-in server settings to this location for customization. 
    mcp_script = readTextFile(user_mcp_server if os.path.isfile(user_mcp_server) else builtin_mcp_server)
    mcp_script = mcp_script.replace("mcp.run(show_banner=False)", f'''mcp.run(show_banner=False, transport="http", host="0.0.0.0", port={args.port if args.port else config.mcp_port})''')
    exec(mcp_script)

if __name__ == "__main__":
    mcp()