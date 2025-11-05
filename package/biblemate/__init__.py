from agentmake import USER_OS, AGENTMAKE_USER_DIR, readTextFile, writeTextFile
from pathlib import Path
from biblemate import config
from biblemate.ui.selection_dialog import TerminalModeDialogs
import os, shutil, pprint
import warnings

# Filter out the specific RuntimeWarning from the 'agentmake' module
warnings.filterwarnings(
    "ignore", 
    message="coroutine '.*' was never awaited", 
    category=RuntimeWarning, 
    module='agentmake'
)

BIBLEMATE_USER_DIR = os.path.join(AGENTMAKE_USER_DIR, "biblemate")
if not os.path.isdir(BIBLEMATE_USER_DIR):
    Path(BIBLEMATE_USER_DIR).mkdir(parents=True, exist_ok=True)
CONFIG_FILE_BACKUP = os.path.join(BIBLEMATE_USER_DIR, "biblemate.config")

# NOTE: When add a config item, update both `write_user_config` and `default_config`

def write_user_config():
    """Writes the current configuration to the user's config file."""
    configurations = f"""config.banner_title="{config.banner_title}"
config.agent_mode={config.agent_mode}
config.prompt_engineering={config.prompt_engineering}
config.auto_suggestions={config.auto_suggestions}
config.auto_tool_selection={config.auto_tool_selection}
config.max_steps={config.max_steps}
config.light={config.light}
config.web_browser={config.web_browser}
config.hide_tools_order={config.hide_tools_order}
config.skip_connection_check={config.skip_connection_check}
config.default_bible="{config.default_bible}"
config.default_commentary="{config.default_commentary}"
config.default_encyclopedia="{config.default_encyclopedia}"
config.default_lexicon="{config.default_lexicon}"
config.max_semantic_matches={config.max_semantic_matches}
config.max_log_lines={config.max_log_lines}
config.mcp_port={config.mcp_port}
config.mcp_timeout={config.mcp_timeout}
config.color_agent_mode="{config.color_agent_mode}"
config.color_partner_mode="{config.color_partner_mode}"
config.color_info_border="{config.color_info_border}"
config.embedding_model="{config.embedding_model}"
config.custom_input_suggestions={pprint.pformat(config.custom_input_suggestions)}
config.disabled_tools={pprint.pformat(config.disabled_tools)}"""
    writeTextFile(CONFIG_FILE_BACKUP, configurations)

# restore config backup after upgrade
default_config = '''config.banner_title=""
config.agent_mode=False
config.prompt_engineering=False
config.auto_suggestions=True
config.auto_tool_selection=False
config.max_steps=50
config.light=True
config.web_browser=False
config.hide_tools_order=True
config.skip_connection_check=False
config.default_bible="NET"
config.default_commentary="CBSC"
config.default_encyclopedia="ISB"
config.default_lexicon="Morphology"
config.max_semantic_matches=15
config.max_log_lines=2000
config.mcp_port=33333
config.mcp_timeout=9999999999
config.color_agent_mode="#FF8800"
config.color_partner_mode="#8000AA"
config.color_info_border="bright_blue"
config.embedding_model="paraphrase-multilingual"
config.custom_input_suggestions=[]
config.disabled_tools=['search_1_chronicles_only',
'search_1_corinthians_only',
'search_1_john_only',
'search_1_kings_only',
'search_1_peter_only',
'search_1_samuel_only',
'search_1_thessalonians_only',
'search_1_timothy_only',
'search_2_chronicles_only',
'search_2_corinthians_only',
'search_2_john_only',
'search_2_kings_only',
'search_2_peter_only',
'search_2_samuel_only',
'search_2_thessalonians_only',
'search_2_timothy_only',
'search_3_john_only',
'search_acts_only',
'search_amos_only',
'search_colossians_only',
'search_daniel_only',
'search_deuteronomy_only',
'search_ecclesiastes_only',
'search_ephesians_only',
'search_esther_only',
'search_exodus_only',
'search_ezekiel_only',
'search_ezra_only',
'search_galatians_only',
'search_genesis_only',
'search_habakkuk_only',
'search_haggai_only',
'search_hebrews_only',
'search_hosea_only',
'search_isaiah_only',
'search_james_only',
'search_jeremiah_only',
'search_job_only',
'search_joel_only',
'search_john_only',
'search_jonah_only',
'search_joshua_only',
'search_jude_only',
'search_judges_only',
'search_lamentations_only',
'search_leviticus_only',
'search_luke_only',
'search_malachi_only',
'search_mark_only',
'search_matthew_only',
'search_micah_only',
'search_nahum_only',
'search_nehemiah_only',
'search_numbers_only',
'search_obadiah_only',
'search_philemon_only',
'search_philippians_only',
'search_proverbs_only',
'search_psalms_only',
'search_revelation_only',
'search_romans_only',
'search_ruth_only',
'search_song_of_songs_only',
'search_titus_only',
'search_zechariah_only',
'search_zephaniah_only']'''

def load_config():
    """Loads the user's configuration from the config file."""
    if not os.path.isfile(CONFIG_FILE_BACKUP):
        exec(default_config, globals())
        write_user_config()
    else:
        exec(readTextFile(CONFIG_FILE_BACKUP), globals())
    # check if new config items are added
    changed = False
    for config_item in default_config[7:].split("\nconfig."):
        key, _ = config_item.split("=", 1)
        if not hasattr(config, key):
            exec(f"config.{config_item}", globals())
            changed = True
    if changed:
        write_user_config()

# load user config at startup
load_config()

# temporary config
config.current_prompt = ""
config.cancelled = False
config.last_multi_bible_selection = [config.default_bible]
config.last_bible_reference = ""
config.last_book = 43
config.last_chapter = 3
config.last_verse = 16
config.backup_required = False
config.export_item = ""
config.action_list = {
    # general
    ".ideas": "generate ideas for prompts to try",
    ".exit": "exit current prompt",
    # conversations
    ".new": "new conversation",
    ".trim": "trim conversation",
    ".edit": "edit conversation",
    ".reload": "reload conversation",
    ".import": "import conversation",
    ".export": "export conversation",
    ".backup": "backup conversation",
    ".find": "search conversation",
    # UBA content
    ".bible": "open bible verse",
    ".chapter": "open bible chapter",
    ".compare": "compare bible verse in different versions",
    ".comparechapter": "compare bible chapter in different versions",
    ".xref": "open cross-references",
    ".treasury": "open treasury of scripture knowledge",
    ".commentary": "open commentary",
    ".aicommentary": "open AI commentary",
    ".index": "open verse study indexes",
    ".translation": "open interlinear, literal & dynamic translations",
    ".discourse": "open discourse analysis",
    ".morphology": "open morphology data",
    ".search": "search bible",
    ".dictionary": "search dictionary",
    ".encyclopedia": "search encyclopedia",
    ".lexicon": "search lexicon",
    ".parallel": "search parallel passages",
    ".promise": "search bible promises",
    ".topic": "search bible topic",
    ".name": "search bible name",
    ".character": "search bible character",
    ".location": "search bible location",
    ".chronology": "open bible chronology",
    ".defaultbible": "configure default bible",
    ".defaultcommentary": "configure default commentary",
    ".defaultencyclopedia": "configure default encyclopedia",
    ".defaultlexicon": "configure default lexicon",
    # resource information
    ".tools": "list available tools",
    ".plans": "list available plans",
    ".resources": "list UniqueBible resources",
    # configurations
    ".backend": "configure backend",
    ".steps": "configure the maximum number of steps allowed",
    ".matches": "configure the maximum number of semantic matches",
    ".mode": "configure AI mode",
    #".agent": "switch to agent mode",
    #".partner": "switch to partner mode",
    #".chat": "switch to chat mode",
    ".autosuggest": "toggle auto input suggestions",
    ".autoprompt": "toggle auto prompt engineering",
    ".autotool": "toggle auto tool selection in chat mode",
    ".light": "toggle light context",
    # file access
    ".content": "show current directory content",
    ".open": "open file or folder",
    ".download": "download data files",
    # help
    ".help": "help page",
}

# copy etextedit plugins
ETEXTEDIT_USER_PULGIN_DIR = os.path.join(os.path.expanduser("~"), "etextedit", "plugins")
if not os.path.isdir(ETEXTEDIT_USER_PULGIN_DIR):
    Path(ETEXTEDIT_USER_PULGIN_DIR).mkdir(parents=True, exist_ok=True)
BIBLEMATE_ETEXTEDIT_PLUGINS = os.path.join(os.path.dirname(os.path.realpath(__file__)), "etextedit", "plugins")
for file_name in os.listdir(BIBLEMATE_ETEXTEDIT_PLUGINS):
    full_file_name = os.path.join(BIBLEMATE_ETEXTEDIT_PLUGINS, file_name)
    if file_name.endswith(".py") and os.path.isfile(full_file_name) and not os.path.isfile(os.path.join(ETEXTEDIT_USER_PULGIN_DIR, file_name)):
        shutil.copy(full_file_name, ETEXTEDIT_USER_PULGIN_DIR)

# constants
AGENTMAKE_CONFIG = {
    "stream": True,
    "print_on_terminal": False,
    "word_wrap": False,
}
OLLAMA_NOT_FOUND = "`Ollama` is not found! BibleMate AI uses `Ollama` to generate embeddings for semantic searches. You may install it from https://ollama.com/ so that you can perform semantic searches of the Bible with BibleMate AI."
BIBLEMATE_VERSION = readTextFile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "version.txt"))
BIBLEMATEDATA = os.path.join(AGENTMAKE_USER_DIR, "biblemate", "data")
if not os.path.isdir(BIBLEMATEDATA):
    Path(BIBLEMATEDATA).mkdir(parents=True, exist_ok=True)
BIBLEMATETEMP = os.path.join(os.path.dirname(os.path.realpath(__file__)), "temp")
if not os.path.isdir(BIBLEMATETEMP):
    Path(BIBLEMATETEMP).mkdir(parents=True, exist_ok=True)
DIALOGS = TerminalModeDialogs()

def fix_string(content):
    return content.replace(" ", " ").replace("‑", "-")

def list_dir_content(directory:str="."):
    directory = os.path.expanduser(directory.replace("%2F", "/"))
    if os.path.isdir(directory):
        folders = []
        files = []
        for item in sorted(os.listdir(directory)):
            if os.path.isdir(os.path.join(directory, item)):
                folders.append(f"📁 {item}")
            else:
                files.append(f"📄 {item}")
        return " ".join(folders) + ("\n\n" if folders and files else "") + " ".join(files)
    return "Invalid path!"