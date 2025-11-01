# 🛠️ Customization

BibleMate AI is highly customizable. Advanced users can modify existing tools, create new ones, and even change the behavior of the AI agent by customizing system prompts.

Custom files are placed in the `biblemate` sub-directory within the AgentMake user directory (typically `~/.agentmake/biblemate` on Linux/macOS or `%USERPROFILE%\.agentmake\biblemate` on Windows).

## Main Configuration File

Main configuration settings are stored in the file:

`~/.agentmake/biblemate/biblemate.config` (on Linux/macOS)

`%USERPROFILE%\.agentmake\biblemate\biblemate.config` (on Windows)

You may manually edit this file to change a certain settings.

For example, you can customize the border colors of agent and partner modes, by changing the values of `color_agent_mode` and `color_partner_mode` in the this file.

## Frequently Used Prompts and Plans

You can save, search, open or delete frequently used prompts and plans.

For examples:

* Enter a prompt and use `Ctrl+W` to save a prompt.
* Prefix a prompt with `@@` and use `Ctrl+W` to save a prompt.
* Use `Esc+W` to delete a saved prompt / plan.
* Use `Ctrl+L` to open a prompt / plan.
* Use `Esc+L` to search for prompts / plans.

## Override system prompts

The agent's core logic is guided by system prompts, which are markdown files. You can override them by placing your own versions in `~/.agentmake/systems/biblemate/`.

The customizable system prompt files are: `supervisor.md`, `tool_instruction.md`, and `tool_selection.md`. You can copy them from the `biblemate/systems` directory in the package installation folder to your user directory and modify them as needed.

## Add or Modify Tools & Plans

You can add your own tools and built-in plans (prompts) by creating a custom `bible_study_mcp.py` file.

1.  First, locate the built-in `bible_study_mcp.py` file inside the `biblemate` package installation directory.
2.  Copy this file to your user customization directory at `~/.agentmake/biblemate/bible_study_mcp.py`.
3.  Now you can edit this file to add or modify tools and prompts using the `fastmcp` syntax. BibleMate AI will automatically load your custom file instead of the built-in one.

## Use http as transport instead of stdio

BibleMate use `stdio` as the default transport for interacting with BibleMate MCP server.  You may use `http` instead.

Run in a thread:

> biblematemcp

Run in another thread:

> biblemate -mcp biblemate

## Use Local Bible Data

Read [HERE](https://github.com/eliranwong/biblemate/issues/15#issuecomment-3314130281) for more details.

## Use Custom MCP Server

You may use a custom MCP server via CLI option `mcp`, e.g.:

> biblemate -mcp http://127.0.0.1:33333/mcp

## Host or Run a BibleMate MCP Server

Use default port `33333`:

> biblematemcp

The default port can be edited in the configuration file `config.py`.

To override the default port temporaily, e.g.:

> biblematemcp -p 33334