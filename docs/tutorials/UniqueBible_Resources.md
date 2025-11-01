# ✝️ UniqueBible Resources

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

# Keyboard Shortcuts

Most of UniqueBible App's resources can be accessed via hotkeys:

`Ctrl+B` opens Bible options [Mnemonic: B -> Bible]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2016b4cc-f370-4aa1-bcd9-8b8b30f8a727" />

`Ctrl+C` opens the Bible commentary function [Mnemonic: C -> Commentary]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/9a175b0e-7385-4aaa-9f6e-00f57ae675fa" />

`Ctrl+V` opens the single verse study function [Mnemonic: V -> Verse]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/2089542c-573d-47f7-ae57-4704295b9417" />

`Ctrl+X` opens the cross-reference function [Mnemonic: X -> Cross-references]
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/aa2e31fb-e89c-4af8-bd5e-53e631fc12ce" />

`Ctrl+F` searches the Bible database [Mnemonic: F -> Find]. This feature requires additional setup, please refer to https://github.com/eliranwong/biblemate/blob/main/docs/installation/macOS.md#%E6%94%AF%E6%8F%B4%E8%AA%9E%E7%BE%A9%E6%90%9C%E7%B4%A2-semantic-searches-optional
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/a5005066-029f-432f-88a2-771dddd52f8f" />
