# ✒️ Built-in Text Editor

<img width="866" height="629" alt="Image" src="https://github.com/user-attachments/assets/d62658d0-10df-4e56-8de3-58787600327f" />

You can edit current prompt with our built-in text editor, by either enter `.editprompt` or pressing `Ctrl+O` in the BibleMate AI prompt field.

You can also launch the built-in editor on its own by running `etextedit`.

You can use plugins that built with BibleMate AI and AgentMake AI in our built-in text editor `etextedit`.

Plugins `Extract Bible References` and `Insert Bible Text` are installed with BibleMate AI.

You may also add you own `etextedit` plugins and place them into `~/etextedit/plugins`.

Read more about `etextedit` at https://github.com/eliranwong/etextedit 

# Export to DOCX or PDF [Optional]

`etextedit` offers options for exporting content into DOCX and PDF files.

- `pandoc` is required to export content to DOCX format. To install, for example, on Debian/Ubuntu:

> sudo apt install pandoc

- `pdflatex` is required to export content to PDF format. To install, for example, on Debian/Ubuntu:

> sudo apt install texlive-full

# Third-Party Text Editor [Optional]

You can use a third-party text editor of your own choice. Enter `.backend` in the BibleMate AI prompt and specify the value of `DEFAULT_TEXT_EDITOR` with a command that calls your favorite text editor, e.g. `micro -softwrap true -wordwrap true`. To use the built-in text editor `etextedit` for making changes, you simply need one step, i.e. either save `Ctrl+S` or exit `Ctrl+Q`, to return to the BibleMate AI prompt. With third-party text editor, however, you need to save the changes first before exiting.
