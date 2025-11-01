# 🏃 Action Menu

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
| `.autotool`          | Toggle auto tool selection         |
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

## Remarks:

* Enter `.` to open action menu for selecting an action.
* Use `.light` to enable or disable *light context*. When *light context* is enabled (default), BibleMate operates slightly faster, with a minor trade-off in tool response quality. When *light context* is disabled, full context is used, which consumes more tokens for processing but delivers higher response quality.
* To use `.import`, you need to specify a python file that contains a saved conversation.  Conversation is saved into a file each time when a backup is executed. Check the message `Conversation backup saved to ...` or locate the backups in `~/agentmake/computemate`. Instead of loading a mere conversation, you can load both a conversation and its master plan. To do so, specify a backup directory path that contains both `conversation.py` and `master_plan.md`.
* To use `.open`, you need to specify a file or a directory that is to be opened.
* `.edit` command allows you to edit the current conversation with our built-in text editor.  You may customize to use your favorite text editor. Enter `.backend` and change the value of `DEFAULT_TEXT_EDITOR` with a command that calls your favorite text editor.
* Use `.autosuggest` to toggle auto input suggestions. If disabled, you can use `TAB` key to open input suggestions menu.
* Use `.reload` to reload the last saved conversation, if any.  It is useful for continuing an unfinished agentic flow after a conversation was broken for any reasons.
* Command `.matches` works for local MCP connection only.  It doesn't apply to remote MCP connection, as the changes in local settings does not affect the settings in remote servers.
* Start your requests with `.` to retrieve bible verses or chapters, or perform a bible search directly, when the content following the `.` does not match the action commands listed above. For examples:
    - Enter `.John 3:16` to read the verse John 3:16
    - Enter `.John 3:16; Rm 5:8` to read the verse John 3:16 and Romans 5:8
    - Enter `.John 3` to read John chapter 3
    - Enter `.John 3, 4` to read John chapter 3 and 4
    - Enter `.Jesus love` to perform a bible search for `Jesus love`