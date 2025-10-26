# BibleMate AI

**BibleMate AI** is a groundbreaking, autonomous AI agent designed to revolutionize your Bible study. It can create study plans, coordinate multiple Bible tools, and take multi-step actions to complete complex Bible-related tasks, such as conducting an in-depth study of a particular Bible passage.

Developer: Eliran Wong

<img width="1732" height="1302" alt="Image" src="https://github.com/user-attachments/assets/cb19d61a-2492-474d-b67a-ef2c59c7bcff" />

## 👀 An Overview

[![Watch the video](https://img.youtube.com/vi/BxpLmpCm4QU/maxresdefault.jpg)](https://youtu.be/BxpLmpCm4QU)

## ✨ Core Features

- **Autonomous AI Agent:** BibleMate AI can work independently to fulfill your bible study requests.
- **Multi-step Task Execution:** It can break down complex tasks into smaller, manageable steps and execute them sequentially.
- **Rich Toolset:** Comes with over 40 built-in bible tools, powered by our comprehensive bible suite, the [UniqueBible App](https://github.com/eliranwong/UniqueBible).
- **Customizable and Extensible:** Advanced users can customize existing tools or add new ones to suit their specific needs.
- **Flexible AI Backend:** Supports a variety of AI backends via [AgentMake AI](https://github.com/eliranwong/agentmake).

## 🖥️ Supported Platforms

- Windows
- macOS
- Linux
- ChromeOS
- Android (via Piexel Terminal / Termux)

### Supported Python versions

- 3.10
- 3.11
- 3.12

## 🧠 Supported AI Backends

Powered by AgentMake AI, BibleMate AI offers users the flexibility to use various AI backends. Read more at https://github.com/eliranwong/agentmake#supported-backends

For comparison, we tested some of the supported backends using the same prompt `In-depth study on Lamentations 3:22-24` in the tests below:

BibleMate AI + `Azure + ChatGPT 5` https://youtu.be/QvPIyHOhrP0

BibleMate AI + `Gemini API + Gemini 2.5 Flash` https://youtu.be/AZ-zEl_StC0

BibleMate AI + `Mistral Large` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `DeepSeek 3.1` https://youtu.be/FUr--ULDCZM

BibleMate AI + `Groq + GPT-OSS 120B` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `Groq + Llama 3.3 70B` https://youtu.be/oKQyIEnMM8M

BibleMate AI + `XAI + Grok 4` https://youtu.be/JgcxciOc_Ys

### Examples on Backend Setup

Read https://github.com/eliranwong/biblemate/tree/main/docs/backends_setup for more details.

### Tips

To get started quickly, we recommend beginning with the `googleai` backend, which has been extensively tested with BibleMate AI. You can obtain a Gemini API key free of charge. For more information, visit: [https://github.com/eliranwong/biblemate/blob/main/docs/backends_setup/googleai.md](https://github.com/eliranwong/biblemate/blob/main/docs/backends_setup/googleai.md).

## 🎬 Demo - Agent Mode

[![Watch the video](https://img.youtube.com/vi/QvPIyHOhrP0/maxresdefault.jpg)](https://youtu.be/QvPIyHOhrP0)

Another example: [In-depth study on Revelation chapter 7](https://github.com/eliranwong/biblemate/blob/main/test/In-depth_study_on_Revelation_7.md)

## 🧩 Agentic Workflow

1.  **BibleMate AI** receives a request from a user.
2.  **BibleMate AI** analyzes the request and determines that it requires multiple steps to complete.
3.  **BibleMate AI** generates a `Master Plan` that outlines the steps needed to complete the request.
4.  **BibleMate AI** sends the `Master Plan` to a supervisor agent, who reviews the prompt and provides suggestions for improvement.
5.  **BibleMate AI** sends the suggestions to a bible tool selection agent, who selects the most appropriate bible tools for each step of the `Master Plan`.
6.  **BibleMate AI** sends the selected bible tools and the `Master Plan` to an instruction generation agent, who converts the suggestions into clear and concise instructions for an AI assistant to follow.
7.  **BibleMate AI** sends the instructions to an AI assistant, who executes the instructions using the selected bible tools.
8.  **BibleMate AI** monitors the progress of the AI assistant and provides additional suggestions or instructions as needed.
9.  Once all steps are completed, **BibleMate AI** provides a concise summary of the results to the user.
10. The user receives the final response, which fully resolves their original request.

### Workflow Diagram

```mermaid
graph TD
    A[User] -- Request --> B(BibleMate AI);
    B -- Generates Master Plan --> B;
    B -- Master Plan --> C(Supervisor Agent);
    C -- Suggestions --> B;
    B -- Suggestions --> D(Bible Tool Selection Agent);
    D -- Selected Tools --> B;
    B -- Master Plan & Selected Tools --> E(Instruction Generation Agent);
    E -- Instructions --> B;
    B -- Instructions --> F(AI Assistant);
    F -- Executes Instructions --> G((Bible Tools));
    B -- Monitors --> F;
    F -- Progress --> B;
    B -- Summary --> A;
```

## 🚀 Quick Start

> pip install --upgrade biblemate

> biblemate

Enter your request in the BibleMate AI prompt.

- Press `Ctrl+S` to submit your request.
- Press `Ctrl+Y` to display help information.

### Set up virtual environment

For example:

```
cd
python3 -m venv biblemate
source biblemate/bin/activate
pip install --upgrade biblemate
export PATH=$PATH:$HOME/biblemate/bin
biblemate
```

### For Android Users

If you find the default transport `stdio` does not work on Pixel Terminal or Termux terminal apps, use the workaround given below:

Workaround: Run the built-in MCP server and the MCP client in two different tabs or sessions.

Run the built-in BibleMate AI MCP server in a session:

> biblematemcp

Run the BibleMate AI interface in another session:

> biblemate -mcp biblemate

### Support Using Vertex AI

Run:

> pip install --upgrade "biblemate[genai]"

### Upgrade

Run again:

> pip install --upgrade biblemate

### For Developer

> pip install -e .

## ⚙️ Configure AI Backend

After BibleMate AI is launched, enter:

> .backend

A text editor is opened for you to edit the AgentMake AI settings. Change the `DEFAULT_AI_BACKEND` to your own choice of AI backend and enter API keys where appropriate.

You may override the default AI backend temporarily by using the CLI option `-b` or `--backend`. For example,

> biblemate -b groq

### Configure UBA API [Optional]

You can optionally configure the UBA API backend by editing the following items:

```
# Tool: UBA API
UBA_API_LOCAL_PORT=8080
UBA_API_ENDPOINT="https://bible.gospelchurch.uk/plain"
UBA_API_TIMEOUT=10
UBA_API_PRIVATE_KEY=
```

### Configure Remote MCP Server Authentication [Optional]

You can optionally configure the authentication information for the remote MCP server by editing the following items:

```
# BibleMate AI
BIBLEMATE_STATIC_TOKEN=
BIBLEMATE_MCP_PUBLIC_KEY=
BIBLEMATE_MCP_PRIVATE_KEY=
BIBLEMATE_MCP_ISSUER=
BIBLEMATE_MCP_AUDIENCE=
```

## 🗣️ AI Modes

You can select between three AI modes to suit your preferences:

*   **Chat mode** – Provides direct text responses without using tools, ideal for simple queries.
*   **Agent mode** – A fully autonomous agent designed to plan, orchestrate tools, and take multiple actions to address user requests.
*   **Partner mode** – A semi-automated mode that involves you in the process with review and edit prompts, giving you more control over the AI's actions.

`Partner mode` is set as the default on fresh installation.

To switch between modes, use the `.mode` command in the BibleMate AI prompt. This will open a selection dialog where you can choose your preferred mode.

<img width="714" height="271" alt="Image" src="https://github.com/user-attachments/assets/f836a0ad-ae77-4b07-bb74-f9af5bce26c6" />

To help users stay aware of the current AI mode, the input border color changes when switching between modes.

<img width="1732" height="1258" alt="Image" src="https://github.com/user-attachments/assets/0b765955-02e5-4eee-95ca-8cdc5216dd1a" />

You can customize the border colors of agent and partner modes in `config.py`, by changing the values of `color_agent_mode` and `color_partner_mode`.

## 📚 Built-in Tools & Plans

### Built-in Tools

To see the full list of built-in tools and their descriptions, please see the [TOOLS.md](TOOLS.md) file.

To enable or disable some of the tools, enter `.tools` in the BibleMate AI prompt.

When `agent mode` is enabled, all enabled built-in tools are considered and automatically selected for each step in fulfilling the user’s request.

### Built-in Plans

Built-in plans are predefined, frequently used 'master plans' that users can quickly access. Currently, we have added two built-in plans for demonstration purposes. Users can add their own plans via [customization](https://github.com/eliranwong/biblemate#customization).

Starts your prompt with a forward slash `/` to call a plan, e.g.:

> /simple_bible_study John 3:16

> /bible_devotion Deut 6:4

## 🛠️ Single Tool Selection

In some cases, you may want to specify a particular tool for a simple task, rather than having multiple tools automatically selected in the fully automatic `agent mode`.

You can specify a single tool by prefixing a tool name with `@` at the beginning of your prompt. For example,

```
@retrieve_bible_cross_references Deut 6:4; John 3:16
```

Watch this video: https://youtu.be/50m1KRj6uhs

BibleMate AI can also automatically select a single tool to address your request. Simply begin your request with `@` followed by a space, instead of specifying a tool name. For example,

```
@ Read Deut 6:4; John 3:16
```

## 📝 Custom Master Plan

In some cases, you may want to specify a `custom plan` with multiple tools specified for different steps for a complex task, rather than having a `master plan` automatically generated in fully automatic agent mode.

You can use a custom 'Master Plan' of your own, instead of one generated by BibleMate AI. To do this, start your BibleMate AI prompt with '@@' followed by your own master plan for a Bible study. 

For example,

```
@@ Analyze John 3:16 with the following steps: 
1. Call tool 'retrieve_english_bible_verses' for Bible text, 
2. Call tool 'retrieve_bible_cross_references' for Bible cross-references, 
3. Call tool 'interpret_new_testament_verse' for interpretation, and 
4. Call tool 'write_bible_theology' to explain its theology.
```

Watch this video: https://youtu.be/Lejq0sAx030

Another example:

```
@@ Write touching devotion on Deuteronomy 6:4 with the following steps:
1. Analyze the themes using @study_old_testament_themes
2. Identify and explain key biblical keywords from the passage using @identify_bible_keywords
3. Write insights for the devotion using @write_bible_insights
4. Relate the passage to daily life using @write_bible_applications
5. Compose a touching devotion using @write_bible_devotion.
Ensure each step is clearly addressed and the final output is cohesive and inspiring
```

Watch this video: https://youtu.be/NYPyujFG09E

The '@@' trick works even when you are using 'chat' mode with 'agent' mode disabled.

## 🏃 Action Menu

| Command              | Description                        |
|----------------------|------------------------------------|
| `.new`               | New conversation                   |
| `.exit`              | Quit BibleMate AI                  |
| `.backend`           | Change backend                     |
| `.mode`              | Change AI mode                     |
| `.tools`             | List available tools               |
| `.plans`             | List available plans               |
| `.resources`         | List available resources           |
| `.editprompt`        | Edit current prompt                |
| `.backup`            | Backup conversation                |
| `.reload`            | Reload current conversation        |
| `.edit`              | Edit current conversation          |
| `.trim`              | Trim current conversation          |
| `.import`            | Import conversation                |
| `.export`            | Export conversation                |
| `.find`              | Search conversation                |
| `.content`           | Show current directory content     |
| `.open`              | Open file or directory             |
| `.ideas`             | Generate ideas                     |
| `.autosuggest`       | Toggle auto input suggestions      |
| `.autoprompt`        | Toggle auto prompt engineering     |
| `.light`             | Toggle light context               |
| `.steps`             | Set max number of steps            |
| `.matches`           | Set max number of semantic matches |
| `.download`          | Download data files                |
| `.help`              | Show help page                     |

Some commands are designed for retrieving content from UniqueBible App:

| Command              | Description                        |
|----------------------|------------------------------------|
| `.bible`             | Open bible verse                   |
| `.chapter`           | Open bible chapter                 |
| `.compare`           | Compare bible verse                |
| `.comparechapter`    | Compare bible chapter              |
| `.chronology`        | Open Bible Chronology              |
| `.commentary`        | Open commentary                    |
| `.aicommentary`      | Open AI commentary                 |
| `.index`             | Open verse study indexes           |
| `.translation`       | Open interlinear and translations  |
| `.discourse`         | Open discourse analysis            |
| `.morphology`        | Open morphology data               |
| `.xref`              | Open cross-references              |
| `.treasury`          | Open TSKE                          |
| `.search`            | Search bible                       |
| `.parallel`          | Search bible parallels             |
| `.promise`           | Search bible promises              |
| `.dictionary`        | Search dictionary                  |
| `.encyclopedia`      | Search encyclopedia                |
| `.lexicon`           | Search lexicon                     |
| `.topic`             | Search bible topics                |
| `.name`              | Search bible names                 |
| `.character`         | Search bible characters            |
| `.locations`         | Search bible locations             |

Key bindings `Ctrl+B`, `Ctrl+C`, `Ctrl+V` and `Ctrl+X` are designed for opening UBA content in BibleMate AI [[Read](https://github.com/eliranwong/biblemate#%EF%B8%8F-keyboard-shortcuts)].

### Remarks:

* Use `.light` to enable or disable *light context*. When *light context* is enabled (default), BibleMate operates slightly faster, with a minor trade-off in tool response quality. When *light context* is disabled, full context is used, which consumes more tokens for processing but delivers higher response quality.
* To use `.import`, you need to specify a python file that contains a saved conversation.  Conversation is saved into a file each time when a backup is executed. Check the message `Conversation backup saved to ...` or locate the backups in `~/agentmake/computemate`. Instead of loading a mere conversation, you can load both a conversation and its master plan. To do so, specify a backup directory path that contains both `conversation.py` and `master_plan.md`.
* To use `.open`, you need to specify a file or a directory that is to be opened.
* `.edit` command allows you to edit the current conversation with our built-in text editor.  You may customize to use your favorite text editor. Enter `.backend` and change the value of `DEFAULT_TEXT_EDITOR` with a command that calls your favorite text editor.
* Use `.autosuggest` to toggle auto input suggestions. If disabled, you can use `TAB` key to open input suggestions menu.
* Use `.reload` to reload the last saved conversation, if any.  It is useful for continuing an unfinished agentic flow after a conversation was broken for any reasons.
* Command `.matches` works for local MCP connection only.  It doesn't apply to remote MCP connection, as the changes in local settings does not affect the settings in remote servers.
* Start your requests with `.` to retrieve bible verses or chapters, or perform a bible search directly, when the content following the `.` does not match the action commands listed above. For examples:
    - Enter `.John 3:16` to read the verse John 3:16
    - Enter `.John 3` to read John chapter 3
    - Enter `.Jesus love` to perform a bible search for `Jesus love`

## ✝️ UniqueBible Resources

We bring the best of both worlds together in BibleMate AI to enhance your Bible studies. In addition to dynamic AI tools, we have integrated direct access to most [UniqueBible resources](https://github.com/eliranwong/UniqueBible) via BibleMate AI prompts. At any point during a conversation with the AI agent, you can incorporate UniqueBible App data directly into the discussion to enrich the study flow and content.

Type `.resources` in the BibleMate AI prompt to view the available resources. The number of available UniqueBible resources depends on which [UniqueBible web server](https://github.com/eliranwong/UniqueBible) you configured in the backend settings. By default, BibleMate AI uses the UniqueBible web server running at https://bible.gospelchurch.uk. The UniqueBible server is highly customizable; you may set up a local server with your custom resources to use with BibleMate AI.

To connect BibleMate AI with your local server, enter `.backend` in the BibleMate AI prompt, locate the session below, and fill in your local server details:

```
# Tool: UBA API
UBA_API_LOCAL_PORT=8080
UBA_API_ENDPOINT="http://127.0.0.1:8080/plain"
UBA_API_TIMEOUT=10
UBA_API_PRIVATE_KEY=
```

Tips: Start your prompt with `//` to view available resources from the input suggestions.

## 🔎 Semantic Searches [Optional]

To enable semantic searches, you need two things:

1. Install Ollama - BibleMate AI uses `Ollama` to generate embeddings for semantic searches. You may find instruction at https://ollama.com/.
2. Download a few data files. Type `.download` in the BibleMate AI prompt and follow the pop‑up dialog to download them.

<img width="510" height="326" alt="Image" src="https://github.com/user-attachments/assets/ee05517f-1d48-47d1-85e8-5c134a646e03" />

You can also download the files manually, unzip them, and place them in the directory `~/agentmake/biblemate/data`, where `~` represents the user's home directory:

[bible.db](https://drive.google.com/file/d/1E6pDKfjUMhmMWjjazrg5ZcpH1RBD8qgW/view?usp=sharing)

Examples:

> @search_the_whole_bible God create

> //john/KJV/Jesus love

[collection.db](https://drive.google.com/file/d/1y4txzRzXTBty0aYfFgkWfz5qlHERrA17/view?usp=sharing)

Examples:

> //promise/hope

> //parallel/baptism

[dictionary.db](https://drive.google.com/file/d/1UxDKGEQa7UEIJ6Ggknx13Yt8XNvo3Ld3/view?usp=sharing)

Example:

> //dictionary/Israel

[encyclopedia.db](https://drive.google.com/file/d/1NLUBepvFd9UDxoGQyQ-IohmySjjeis2-/view?usp=sharing)

Examples:

> //encyclopedia/Jesus

> //encyclopedia/ISB/Jesus

[exlb.db](https://drive.google.com/file/d/1Hpo6iLSh5KzgR6IZ-c7KuML--A3nmP1-/view?usp=sharing)

Examples:

> //topic/hope

> //name/Bethleham

> //character/Samuel

> //location/Jerusalem

## ⌨️ Keyboard Shortcuts

The following key bindings are supported in BibleMate AI prompt field:

- `Ctrl+Y`: help info
- `Ctrl+S` or `Esc+ENTER` or `Alt+ENTER`: submit input
- `Ctrl+N`: new conversation
- `Esc+I`: import conversation
- `Esc+O`: edit conversation
- `Ctrl+O`: edit input in text editor
- `Ctrl+Q`: exit input
- `Ctrl+R`: reset input
- `Ctrl+Z`: undo input changes
- `Ctrl+W`: save prompt / plan
- `Esc+W`: delete prompt / plan
- `Ctrl+L`: open prompt / plan
- `Esc+L`: search prompt / plan
- `Ctrl+B`: open bible-related features
- `Ctrl+C`: open bible commentaries
- `Ctrl+V`: open bible verse features
- `Ctrl+X`: open cross-references features
- `Ctrl+F`: open search features
- `Ctrl+J`: change AI mode
- `Ctrl+G`: toggle auto input suggestions
- `Esc+G`: generate ideas for prompts to try
- `Ctrl+P`: toggle auto prompt engineering
- `Esc+P`: improve prompt content
- `Ctrl+D`: delete
- `Ctrl+H`: backspace
- `Ctrl+W`: delete previous word
- `Ctrl+U`: kill text until start of line
- `Ctrl+K`: kill text until end of line
- `Ctrl+A`: go to beginning of line
- `Ctrl+E`: go to end of line
- `Ctrl+LEFT`: go to one word left
- `Ctrl+RIGHT`: go to one word right
- `Ctrl+UP`: scroll up
- `Ctrl+DOWN`: scroll down
- `Shift+TAB`: insert four spaces
- `TAB` or `Ctrl+I`: open input suggestion menu
- `Esc`: close input suggestion menu

### Cancel Loading an AI response

Press `Ctrl+C` once or twice until the loading is cancelled, while you are waiting for a response.

### Common shortcuts on Terminal Apps:

- `Ctrl+Shift+C`: Copy
- `Ctrl+Shift+V`: Paste

## ✒️ Built-in Text Editor

<img width="866" height="629" alt="Image" src="https://github.com/user-attachments/assets/d62658d0-10df-4e56-8de3-58787600327f" />

You can edit current prompt with our built-in text editor, by either enter `.editprompt` or pressing `Ctrl+O` in the BibleMate AI prompt field.

You can also launch the built-in editor on its own by running `etextedit`.

You can use plugins that built with BibleMate AI and AgentMake AI in our built-in text editor `etextedit`.

Plugins `Extract Bible References` and `Insert Bible Text` are installed with BibleMate AI.

You may also add you own `etextedit` plugins and place them into `~/etextedit/plugins`.

Read more about `etextedit` at https://github.com/eliranwong/etextedit 

## Export to DOCX or PDF [Optional]

`etextedit` offers options for exporting content into DOCX and PDF files.

- `pandoc` is required to export content to DOCX format. To install, for example, on Debian/Ubuntu:

> sudo apt install pandoc

- `pdflatex` is required to export content to PDF format. To install, for example, on Debian/Ubuntu:

> sudo apt install texlive-full

## Third-Party Text Editor [Optional]

You can use a third-party text editor of your own choice. Enter `.backend` in the BibleMate AI prompt and specify the value of `DEFAULT_TEXT_EDITOR` with a command that calls your favorite text editor, e.g. `micro -softwrap true -wordwrap true`. To use the built-in text editor `etextedit` for making changes, you simply need one step, i.e. either save `Ctrl+S` or exit `Ctrl+Q`, to return to the BibleMate AI prompt. With third-party text editor, however, you need to save the changes first before exiting.

## 🛠️ Customization

BibleMate AI is highly customizable. Advanced users can modify existing tools, create new ones, and even change the behavior of the AI agent by customizing system prompts.

Custom files are placed in the `biblemate` sub-directory within the AgentMake user directory (typically `~/.agentmake/biblemate` on Linux/macOS or `%USERPROFILE%\.agentmake\biblemate` on Windows).

### Frequently Used Prompts and Plans

You can save, search, open or delete frequently used prompts and plans.

For examples:

* Enter a prompt and use `Ctrl+W` to save a prompt.
* Prefix a prompt with `@@` and use `Ctrl+W` to save a prompt.
* Use `Esc+W` to delete a saved prompt / plan.
* Use `Ctrl+L` to open a prompt / plan.
* Use `Esc+L` to search for prompts / plans.

### Override system prompts

The agent's core logic is guided by system prompts, which are markdown files. You can override them by placing your own versions in `~/.agentmake/systems/biblemate/`.

The customizable system prompt files are: `supervisor.md`, `tool_instruction.md`, and `tool_selection.md`. You can copy them from the `biblemate/systems` directory in the package installation folder to your user directory and modify them as needed.

### Add or Modify Tools & Plans

You can add your own tools and built-in plans (prompts) by creating a custom `bible_study_mcp.py` file.

1.  First, locate the built-in `bible_study_mcp.py` file inside the `biblemate` package installation directory.
2.  Copy this file to your user customization directory at `~/.agentmake/biblemate/bible_study_mcp.py`.
3.  Now you can edit this file to add or modify tools and prompts using the `fastmcp` syntax. BibleMate AI will automatically load your custom file instead of the built-in one.

### Use http as transport instead of stdio

BibleMate use `stdio` as the default transport for interacting with BibleMate MCP server.  You may use `http` instead.

Run in a thread:

> biblematemcp

Run in another thread:

> biblemate -mcp biblemate

### Use Local Bible Data

Read [HERE](https://github.com/eliranwong/biblemate/issues/15#issuecomment-3314130281) for more details.

### Use Custom MCP Server

You may use a custom MCP server via CLI option `mcp`, e.g.:

> biblemate -mcp http://127.0.0.1:33333/mcp

### Host or Run a BibleMate MCP Server

Use default port `33333`:

> biblematemcp

The default port can be edited in the configuration file `config.py`.

To override the default port temporaily, e.g.:

> biblematemcp -p 33334

## 📖 Tutorials

... (coming soon) ...

## 📄 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

BibleMate AI is built upon the foundations of our other projects:
*   [UniqueBible App](https.github.com/eliranwong/UniqueBible)
*   [ComputeMate AI](https.github.com/eliranwong/computemate)
*   [AgentMake AI](https.github.com/eliranwong/agentmake)
*   [AgentMake AI MCP](https.github.com/eliranwong/agentmakemcp)
