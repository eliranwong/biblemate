# 🧠 Supported AI Backends

Powered by AgentMake AI, BibleMate AI offers users the flexibility to use various AI backends. Read more at https://github.com/eliranwong/agentmake#supported-backends

For comparison, we tested some of the supported backends using the same prompt `In-depth study on Lamentations 3:22-24` in the tests below:

BibleMate AI + `Azure + ChatGPT 5` https://youtu.be/QvPIyHOhrP0

BibleMate AI + `Gemini API + Gemini 2.5 Flash` https://youtu.be/AZ-zEl_StC0

BibleMate AI + `Mistral Large` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `DeepSeek 3.1` https://youtu.be/FUr--ULDCZM

BibleMate AI + `Groq + GPT-OSS 120B` https://youtu.be/7sBfj2TMoOE

BibleMate AI + `Groq + Llama 3.3 70B` https://youtu.be/oKQyIEnMM8M

BibleMate AI + `XAI + Grok 4` https://youtu.be/JgcxciOc_Ys

## Examples on Backend Setup

Read https://github.com/eliranwong/biblemate/tree/main/docs/backends_setup for more details.

## Tips

To get started quickly, we recommend beginning with the `googleai` backend, which has been extensively tested with BibleMate AI. You can obtain a Gemini API key free of charge. For more information, visit: [https://github.com/eliranwong/biblemate/blob/main/docs/backends_setup/googleai.md](https://github.com/eliranwong/biblemate/blob/main/docs/backends_setup/googleai.md).

# ⚙️ Configure AI Backend

After BibleMate AI is launched, enter:

> .backend

A text editor is opened for you to edit the AgentMake AI settings. Change the `DEFAULT_AI_BACKEND` to your own choice of AI backend and enter API keys where appropriate.

You may override the default AI backend temporarily by using the CLI option `-b` or `--backend`. For example,

> biblemate -b googleai

## Configure UBA API [Optional]

You can optionally configure the UBA API backend by editing the following items:

```
# Tool: UBA API
UBA_API_LOCAL_PORT=8080
UBA_API_ENDPOINT="https://bible.gospelchurch.uk/plain"
UBA_API_TIMEOUT=10
UBA_API_PRIVATE_KEY=
```

## Configure Remote MCP Server Authentication [Optional]

You can optionally configure the authentication information for the remote MCP server by editing the following items:

```
# BibleMate AI
BIBLEMATE_STATIC_TOKEN=
BIBLEMATE_MCP_PUBLIC_KEY=
BIBLEMATE_MCP_PRIVATE_KEY=
BIBLEMATE_MCP_ISSUER=
BIBLEMATE_MCP_AUDIENCE=
```

## More Examples

Check individual examples at https://github.com/eliranwong/biblemate/tree/main/docs/backends_setup