import os, re
from biblemate import config
from agentmake import PACKAGE_PATH, AGENTMAKE_USER_DIR, readTextFile
from pathlib import Path

# set up user_directory for customisation
user_directory = os.path.join(AGENTMAKE_USER_DIR, "biblemate")
Path(user_directory).mkdir(parents=True, exist_ok=True)

def get_system_progress(master_plan: str) -> str:
    """
    create system prompt for checking the progress
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "biblemate", "supervisor.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "biblemate", "supervisor.md")
    system_progress = readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1).format(master_plan=master_plan)
    if not "Preliminary Action Plan" in master_plan: # custom mcp prompts
        system_progress = system_progress.replace("\n# Master Plan", "\n# Preliminary Action Plan")
    return system_progress

def get_system_make_suggestion(master_plan: str) -> str:
    """
    create system prompt for makding suggestion
    """
    action_plan = re.sub("[# ]*?Measurable Outcome.*?$", "", master_plan, flags=re.DOTALL)
    action_plan = re.sub("[# ]*?Preliminary Action Plan", "", action_plan)
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "biblemate", "make_suggestions.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "biblemate", "make_suggestions.md")
    return readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1).format(action_plan=action_plan)

def get_system_tool_instruction(tool: str, tool_description: str = "") -> str:
    """
    create system prompt for tool instruction
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "biblemate", "tool_instruction.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "biblemate", "tool_instruction.md")
    return readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1).format(tool=tool, tool_description=tool_description)

def get_system_tool_selection(available_tools: list, tool_descriptions: str) -> str:
    """
    create system prompt for tool selection
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "biblemate", "tool_selection_lite.md" if config.light else "tool_selection.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "biblemate", "tool_selection_lite.md" if config.light else "tool_selection.md")
    return readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1).format(available_tools=available_tools, tool_descriptions=tool_descriptions)

def get_system_master_plan() -> str:
    """
    create system prompt for master plan generation
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "create_action_plan.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "create_action_plan.md")
    return readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1)

def get_system_improve_prompt_2() -> str:
    """
    create system prompt for prompt engineering
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "improve_prompt_2.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "improve_prompt_2.md")
    return readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1)

def get_system_generate_title() -> str:
    """
    create system prompt for title generation
    """
    possible_system_file_path_2 = os.path.join(PACKAGE_PATH, "systems", "generate_title.md")
    possible_system_file_path_1 = os.path.join(AGENTMAKE_USER_DIR, "systems", "generate_title.md")
    system_prompt = readTextFile(possible_system_file_path_2 if os.path.isfile(possible_system_file_path_2) else possible_system_file_path_1)
    return system_prompt