# BibleMate AI

**BibleMate AI** is a groundbreaking, autonomous AI agent designed to revolutionize your Bible study. It can create study plans, coordinate multiple Bible tools, and take multi-step actions to complete complex Bible-related tasks, such as conducting an in-depth study of a particular Bible passage.

**🌐 Website:** https://biblemate.ai
**📺 Public Demo:** https://biblemate.gospelchurch.uk
**🔌 MCP Server:** https://bible.gospelchurch.uk/mcp
**📡 API Server:** https://biblemate.gospelchurch.uk/api/data

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Key Features](#key-features)
- [Components & Repositories](#components--repositories)
- [Related Projects](#related-projects)
- [Data Repositories](#data-repositories)

## Overview

BibleMate AI is a comprehensive Bible study suite that represents a major upgrade from the [UniqueBible App](https://github.com/eliranwong/UniqueBible). It offers multiple interfaces and deployment options to suit different use cases:

- **CLI** - Command-line interface for terminal users
- **Web GUI** - Modern web interface accessible from any browser
- **MCP Server** - Model Context Protocol integration for AI assistants
- **HTTP/API Server** - RESTful API for custom integrations

## Getting Started

### Installation

Choose the package(s) that match your needs:

```bash
# CLI Version, Agent Mode, Partner Mode, and MCP Server
pip install --upgrade biblemate

# Bible Data Setup
pip install --upgrade biblematedata

# Web GUI, HTTP Server, API Server
pip install --upgrade biblemateweb
```

### Usage

```bash
# Launch CLI / Agent Mode / Partner Mode
biblemate

# Launch MCP Server
biblematemcp

# Setup Bible Data
biblematedata

# Launch Web GUI / HTTP Server
biblemateweb

# API Client
biblemateapi -h
```

**Access Web Interface:**
- Local: http://localhost:33355
- Public Demo: https://biblemate.gospelchurch.uk

## Key Features

BibleMate AI builds upon the UniqueBible App foundation with extensive new capabilities:

### AI-Powered Study Tools
- **AI Agent Mode** - Autonomous multi-step Bible study assistance
- **AI Partner Mode** - Interactive Bible study companion
- **AI-Generated Content** - Book analysis, chapter summaries, and verse commentary in 3 languages

### Search & Discovery
- **12 Advanced Search Tools** - Comprehensive search capabilities
- **Semantic Search** - Vector database-powered contextual search
- **Morphology Search** - Selective morphological analysis with web UI

### Original Languages
- **Hebrew & Greek Audio** - Quick access via tooltips for every word
- **Parallel Bible Scrolling** - Synchronized viewing across translations
- **Original Text Resources** - Extensive Hebrew and Greek databases

### Audio & Media
- **Bible Podcasts** - Audio for every book and chapter
- **Verse-by-Verse Audio** - Multiple translations and accents
- **Audio Loop Feature** - Enhanced listening experience

### Modern Infrastructure
- **MCP Server** - Model Context Protocol integration
- **Rewritten API** - Modern RESTful API server
- **Rewritten Web GUI** - Enhanced user interface
- **Cloud Sync** - Bible notes synchronization with Google accounts
- **User Customization** - Personalized web UI settings

### Enhanced Visualization
- Bible relationships, maps, timelines, and chronology
- Improved tab and history management
- One-click data downloads

## Components & Repositories

BibleMate AI consists of three main components, each maintained in separate repositories:

### 1. CLI & MCP Server
**Repository:** https://github.com/eliranwong/biblematecli
**Package:** `biblemate`
**Includes:** Command-line interface, Agent Mode, Partner Mode, MCP Server

```bash
pip install --upgrade biblemate
biblemate           # Launch CLI
biblematemcp        # Launch MCP Server
```

### 2. Web GUI & API Server
**Repository:** https://github.com/eliranwong/biblemateweb
**Package:** `biblemateweb`
**Includes:** Web interface, HTTP server, API server, API client

```bash
pip install --upgrade biblemateweb
biblemateweb        # Launch web server
biblemateapi -h     # API client help
```

### 3. Bible Data
**Repository:** https://github.com/eliranwong/biblematedata
**Package:** `biblematedata`
**Includes:** Data setup and management tools

```bash
pip install --upgrade biblematedata
biblematedata       # Setup Bible data
```


## Related Projects

BibleMate AI builds upon and integrates with several projects:

### Foundation Projects
- [UniqueBible App](https://github.com/eliranwong/UniqueBible) - Original Bible study application
- [UniqueBible API](https://github.com/eliranwong/UniqueBibleAPI) - API foundation
- [Marvel Bible Resources](https://github.com/eliranwong/Marvel.bible) - Comprehensive Bible resources

### AI Framework Integration
- [ComputeMate AI](https://github.com/eliranwong/computemate) - AI computation framework
- [AgentMake AI](https://github.com/eliranwong/agentmake) - AI agent framework
- [AgentMake AI MCP](https://github.com/eliranwong/agentmakemcp) - MCP integration
- [TeamGen AI](https://github.com/eliranwong/teamgenai) - Multi-agent collaboration

### Bible-Specific Tools
- [SearchBible AI](https://github.com/eliranwong/searchbibleai) - AI-powered Bible search
- [Bible Verse Parser](https://github.com/eliranwong/bible-verse-parser) - Verse reference parsing
- [eTextEdit](https://github.com/eliranwong/etextedit) - Text editing utilities

### Internationalization
CLI versions are also available in Chinese:

- [Traditional Chinese CLI](https://github.com/eliranwong/biblematetc)
- [Simplified Chinese CLI](https://github.com/eliranwong/biblematesc)

*Note: The English version works with BibleMate web server. Chinese versions currently work with UniqueBible App web server.*

## Data Repositories

BibleMate AI provides access to extensive Bible data resources across multiple repositories:

### Hebrew & Greek Texts
- [Open Hebrew Bible](https://github.com/eliranwong/OpenHebrewBible) - Tagged Hebrew Bible
- [Open GNT](https://github.com/eliranwong/OpenGNT) - Open Greek New Testament
- [LXX Rahlfs 1935](https://github.com/eliranwong/LXX-Rahlfs-1935) - Septuagint (Rahlfs edition)
- [LXX Swete 1930](https://github.com/eliranwong/LXX-Swete-1930) - Septuagint (Swete edition)
- [SBLGNT Add-ons](https://github.com/eliranwong/SBLGNT-add-ons) - SBL Greek New Testament enhancements

### AI-Generated Content
- [Bible Book Analysis](https://github.com/eliranwong/BibleBookStudies) - AI analysis of every book
- [Bible Chapter Summaries](https://github.com/eliranwong/BibleChapterSummaries) - AI summaries of every chapter
- [Bible Verse Commentary](https://github.com/eliranwong/AI_Commentary) - AI commentary on every verse

### Markdown Bibles
- [KJV in Markdown](https://github.com/eliranwong/markdown_bible_KJV)
- [NET in Markdown](https://github.com/eliranwong/markdown_bible_NET)

### Audio Bibles

**English Translations:**
- [ASV](https://github.com/eliranwong/MP3_AmericanStandardVersion_american) - American accent, verse-by-verse
- [BBE](https://github.com/eliranwong/MP3_BibleInBasicEnglish_british) - British accent, verse-by-verse
- [BSB](https://github.com/eliranwong/MP3_BereanStudyBible_american) / [BSB British](https://github.com/eliranwong/MP3_BereanStudyBible_british)
- [ERV](https://github.com/eliranwong/MP3_EnglishRevisedVersion_british) - British accent, verse-by-verse
- [ISV](https://github.com/eliranwong/MP3_InternationalStandardVersion_american) / [ISV British](https://github.com/eliranwong/MP3_InternationalStandardVersion_british)
- [KJV](https://github.com/eliranwong/MP3_KingJamesVersion_american) / [KJV British](https://github.com/eliranwong/MP3_KingJamesVersion_british)
- [LEB](https://github.com/eliranwong/MP3_LexhamEnglishBible_american) / [LEB British](https://github.com/eliranwong/MP3_LexhamEnglishBible_british)
- [NET](https://github.com/eliranwong/MP3_NewEnglishTranslation_american) / [NET British](https://github.com/eliranwong/MP3_NewEnglishTranslation_british)
- [WEB](https://github.com/eliranwong/MP3_WebEnglishBible_british) - British accent, verse-by-verse

**Original Languages:**
- [BHS5](https://github.com/eliranwong/MP3_BHS5_word-by-word) - Hebrew, word-by-word
- [OGNT](https://github.com/eliranwong/MP3_OpenGNT_word-by-word) - Greek, word-by-word
- [OHGB Fast](https://github.com/eliranwong/MP3_OpenHebrewGreekBible_fast) / [OHGB Slow](https://github.com/eliranwong/MP3_OpenHebrewGreekBible_slow) - Hebrew & Greek
- [SBLGNT Fast](https://github.com/eliranwong/MP3_SBLGNT_fast) / [SBLGNT Slow](https://github.com/eliranwong/MP3_SBLGNT_slow) - Greek
- [WLC Fast](https://github.com/eliranwong/MP3_WLC_fast) / [WLC Slow](https://github.com/eliranwong/MP3_WLC_slow) - Hebrew

**Chinese:**
- [CUV Cantonese](https://github.com/eliranwong/MP3_ChineseUnionVersion_cantonese)
- [CUV Mandarin](https://github.com/eliranwong/MP3_ChineseUnionVersion_mandarin)

**Chapter Podcasts:**
- [Daniel](https://github.com/eliranwong/Bible_Podcast_Daniel)
- [The Twelve](https://github.com/eliranwong/Bible_Podcast_The_Twelve)
- [Ruth](https://github.com/eliranwong/Bible_Podcast_Ruth)
- [Numbers](https://github.com/eliranwong/Bible_Podcast_Numbers)
- [Leviticus](https://github.com/eliranwong/Bible_Podcast_Leviticus)
- [Hebrews](https://github.com/eliranwong/Bible_Podcast_Hebrews)
- [Gospel of Mark](https://github.com/eliranwong/Bible_Podcast_Gospel_of_Mark)
- [Exodus](https://github.com/eliranwong/Bible_Podcast_Exodus)
- [Catholic Letters](https://github.com/eliranwong/Bible_Podcast_Catholic_Letters)

### Specialized Collections

**Bible Promises:**
- [Take Words with You](https://github.com/eliranwong/take-words-with-you)
- [Precious Bible Promises](https://github.com/eliranwong/Precious-Bible-Promises)

**Parallel Passages:**
- [Gospel Parallels](https://github.com/eliranwong/Chinese_synopsis)
