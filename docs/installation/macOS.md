# Installing BibleMate AI on macOS

BibleMate AI supports over a dozen AI providers, such as OpenAI, Google Gemini, xAI, Groq, and more. This page introduces one method that is free and can be installed on a typical computer setup.

BibleMate AI runs on Windows 11, macOS, Linux, ChromeOS, and Android. The basic steps involve the following three:

1. [Register for an AI cloud provider service](https://github.com/eliranwong/biblemate/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%B8%80%E6%AD%A5---%E7%94%B3%E8%AB%8B-google-gemini-api-keys%E5%85%8D%E8%B2%BB) (this step can be skipped if you have a powerful computer).
2. [Install Python 3.10-3.12](https://github.com/eliranwong/biblemate/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%BA%8C%E6%AD%A5---%E5%AE%89%E8%A3%9D-python) (Linux systems usually have Python pre-installed, so this step might be skippable).
3. [Install BibleMate AI](https://github.com/eliranwong/biblemate/blob/main/docs/installation/macOS.md#%E7%AC%AC%E4%B8%89%E6%AD%A5---%E5%AE%89%E8%A3%9D-biblemate-ai-%E4%B8%AD%E6%96%87%E7%89%88)

## Step 1 - Apply for Google Gemini API Keys (Free)

1. Open the website https://aistudio.google.com, select `Get Started`, and log in with your personal Google Account.
<img width="1281" height="461" alt="Image" src="https://github.com/user-attachments/assets/e9a54d02-c245-4331-9de2-0764e94bc561" />

2. In the left menu, select `Get API Key`, and then in the top right corner, select `Create API Key`.
<img width="1617" height="1056" alt="Image" src="https://github.com/user-attachments/assets/63d5f1ab-9ba1-4eee-a213-af58ccf73541" />

3. First, select `Create Project`, for example, enter: BibleMate.
<img width="512" height="329" alt="Image" src="https://github.com/user-attachments/assets/97d677d5-22c5-42b2-b9e7-f7106efcb09c" />

4. Enter an API name for future identification, for example, enter: BibleMate.
<img width="511" height="283" alt="Image" src="https://github.com/user-attachments/assets/9ceb7476-c56c-4459-90bd-69c4b168fceb" />

5. Copy the newly created API Key and save it in your preferred way. It will be useful in the third step. Do not share this API Key with others.
<img width="1043" height="263" alt="Image" src="https://github.com/user-attachments/assets/6373d1ce-f4f6-4529-899a-3d535a513f4a" />

Notes:
* You can ignore Billing, as Google provides a free tier.
* The Free Tier has rate limits with heavy usage. It is recommended that if a family uses it together, they apply for multiple API Keys using different family members' Google Accounts.
* To switch from Google Gemini to other AI providers, please refer to https://github.com/eliranwong/biblemate/tree/main/docs/backends_setup

## Step 2 - Install Python

1. Open [https://python.org](https://python.org), select `Downloads` -> `macOS`. Do not download version 3.14 directly; BibleMate AI currently only supports Python versions 3.10-3.12.
<img width="1503" height="660" alt="Image" src="https://github.com/user-attachments/assets/81f0eb85-20ea-4480-8ff5-17c0d4dac0e6" />

2. Select Download [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.12.10/python-3.12.10-macos11.pkg). You can also choose other versions, but they must be within the 3.10-3.12 range.
<img width="987" height="865" alt="Image" src="https://github.com/user-attachments/assets/b3c7bcbb-da7e-4590-8d74-cce13a269605" />

3. After downloading, find the new file in your computer's Downloads folder, double-click to open it, and follow the instructions to install.
<img width="732" height="556" alt="Image" src="https://github.com/user-attachments/assets/7bed2aea-a381-4fa3-b7b9-c1582b88e3e3" />

## Step 3 - Install BibleMate AI

1. Open the `Terminal` app (`Applications` -> `Utilities` -> `Terminal`).
<img width="1032" height="576" alt="Image" src="https://github.com/user-attachments/assets/126afe61-758e-404d-9e9f-8dccd6e9936d" />

2. After opening, copy the seven lines of commands below, paste them into the Terminal app, and press the `Enter` key to execute.

```
cd
python3 -m venv biblemate
source biblemate/bin/activate
pip install --upgrade pip "biblemate[genai]"
echo "alias bmsc='$HOME/biblemate/bin/bmsc'" >> .zprofile
echo "alias biblemate tc='$HOME/biblemate/bin/biblemate'" >> .zprofile
bmsc
```

3. Allow the Terminal app to connect to the network.
<img width="372" height="360" alt="Image" src="https://github.com/user-attachments/assets/667f10d0-075c-478b-a2f5-717b7decd936" />

4. Enter the Google Gemini API Key you applied for in the first step. If you don't want to type it character by character, you can copy the API Key first, then press `Command+V` to paste it here (please replace xxxxxxxxxxx with your valid API Key):
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/ee882eae-514f-4406-95cf-a40d1fe632ac" />

5. BibleMate AI supports using several API Keys in rotation (separate multiple API Keys with an English comma `,` without spaces):
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/6520bcbf-ee7d-4727-8c1d-2fb36b7e3a69" />

6. After pressing `OK` to confirm, you need to restart. In the Terminal App, type `biblemate` or `bmsc`.
<img width="890" height="124" alt="Image" src="https://github.com/user-attachments/assets/92332717-0011-4504-8bbc-f0b38721e63f" />

## Notes

* All API Keys are only stored on your personal computer, in the file `~/agentmake/agentmake.env`.
* The Terminal app defaults to a white background with black text, and the default font size is very small. I personally recommend changing to a black background with white text and increasing the font size. This can be changed in the Terminal app's Settings.

# Usage

1. In the Terminal app, type `biblemate` or `bmsc` to enter BibleMate AI.
2. Enter your request, then press `Ctrl+S` to confirm and let BibleMate AI execute your request.
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/a2f84f01-e2e4-496e-9359-b8afd5dcc583" />

## Exit Current Entry

Press `Ctrl+Q` to exit current entries.

## Use Built-in Text Editor for Editing

You can press `Ctrl+O` to edit your input with the built-in text editor for more editing features via plugins.

## Manage Conversation

Each of your requests and BibleMate AI's responses are taken into a conversation flow for building context for future requests.

The following entries are designed for conversation management:

| Entries              | Description                        |
|----------------------|------------------------------------|
| `.new`               | New conversation                   |
| `.backup`            | Backup conversation                |
| `.reload`            | Reload current conversation        |
| `.edit`              | Edit current conversation          |
| `.trim`              | Trim current conversation          |
| `.import`            | Import conversation                |
| `.export`            | Export conversation                |
| `.find`              | Search conversation                |

## Switching Between Different AI Modes

BibleMate AI supports three AI modes - Agent, Partner, and Chat - for users to switch between as needed:

* `Agent` mode - Fully automatic mode, where the AI executes all steps.
* `Partner` mode (default) - Semi-automatic operation mode, where the user participates in reviewing and modifying.
* `Chat` mode - A simple question-and-answer dialogue mode.

1. Enter `.mode` to open the AI mode menu:
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/47ecf9ed-fe07-4773-91f6-1cd9a8598d41" />

2. Choose one of the modes.
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/13a07479-1fd9-4cac-b379-c2c16a71525b" />

3. After switching, enter your request, and then press `Ctrl+S` to confirm.
<img width="1002" height="697" alt="Image" src="https://github.com/user-attachments/assets/1514558a-5d8e-472e-b06f-2fb72ebb96dd" />

## Semantic Search Support [Optional]

You can search various biblical resources through BibleMate AI, such as the Bible, original language dictionaries, encyclopedias, biblical promises, etc., but it requires two additional setups:

1. Install Ollama on your computer (BibleMate AI uses Ollama to create a vector database). You can download it from https://ollama.com/download
2. In BibleMate AI, enter the command `.download` and follow the instructions to download the additional databases.
<img width="866" height="629" alt="Image" src="https://github.com/user-attachments/assets/1e8aa6b2-4c47-4fe0-9e9d-7d5163f88ea4" />

## Directly Accessing Bible and Related Resources Without AI

BibleMate AI defaults to connecting to the [Gospel Church UK](https://bible.gospelchurch.uk)'s Bible website https://bible.gospelchurch.uk/traditional.html. Users can directly access Bible study materials at any time without using the AI function.

Most of BibleMate AI's functions can be accessed via hotkeys, five of which are designed for quick access to Bible-related materials:

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

## More Shortcuts

`Ctrl+Y` opens the help menu.

## More Feature Information

Chinese: https://github.com/eliranwong/biblematetc

English: https://github.com/eliranwong/biblemate
