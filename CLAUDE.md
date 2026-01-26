# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **landing page and documentation repository** for BibleMate AI. It does NOT contain the actual application code - only README documentation and metadata.

The BibleMate AI project is a comprehensive Bible study suite with multiple components, each in separate repositories:

- **CLI Version / Agent / Partner / MCP Server**: https://github.com/eliranwong/biblematecli
- **Web GUI / HTTP Server / API Server**: https://github.com/eliranwong/biblemateweb
- **Bible Data**: https://github.com/eliranwong/biblematedata

## Repository Purpose

This repository serves as:
- The main entry point for users discovering BibleMate AI
- Central documentation hub linking to all BibleMate components
- Landing page for the GitHub organization

## Key Information from README

### Installation Commands
```bash
# CLI Version / Agent Mode / Partner Mode / MCP Server
pip install --upgrade biblemate

# Bible Data Setup
pip install --upgrade biblematedata

# Web UI / HTTP Server / API Server
pip install --upgrade biblemateweb
```

### Launch Commands
```bash
# CLI Version / Agent Mode / Partner Mode
biblemate

# MCP Server
biblematemcp

# Data Setup
biblematedata

# HTTP Server / API Server / Web GUI
biblemateweb

# API Client
biblemateapi -h
```

### Web Access
- Local: http://localhost:33355
- Public Demo: https://biblemate.gospelchurch.uk
- MCP Server: https://bible.gospelchurch.uk/mcp
- API Server: https://biblemate.gospelchurch.uk/api/data

## Development Notes

### Repository Structure
This repository contains minimal files:
- `README.md` - Main documentation
- `.github/FUNDING.yml` - GitHub funding configuration
- `.gitignore` - Excludes build artifacts, venv, temp files, and JSON files

### Git Workflow
- Main branch: `main`
- This repo is documentation-only, so commits are typically README updates
- Past commits show this was migrated from UniqueBible App

### Historical Context
BibleMate AI is a full upgrade from the UniqueBible App, with significant enhancements:
- AI Agent Mode and Partner Mode for Bible studies
- MCP Server integration
- Rewritten API, CLI, and Web GUI
- AI-generated content (book analysis, chapter summaries, verse commentary in 3 languages)
- 12 search tools including semantic search with vector database
- Enhanced audio features and visual presentation

### Related Projects
BibleMate AI builds on:
- UniqueBible App (foundation)
- ComputeMate AI, AgentMake AI, TeamGen AI (AI frameworks)
- SearchBible AI, Bible Verse Parser (Bible-specific tools)
- Extensive data repositories (Hebrew/Greek texts, audio Bibles, AI-generated content)

## When Working in This Repo

Since this is a documentation-only repo:
1. Changes will primarily involve updating README.md
2. Keep README structure: overview → features → installation → usage → related projects
3. Maintain consistency in link formatting and organization
4. Preserve the comprehensive listing of related repositories and data sources
5. Ensure version numbers and package names stay synchronized with actual packages

## Working with Actual BibleMate Code

To modify the actual BibleMate applications, clone the relevant repository:
- For CLI/MCP changes: `git clone https://github.com/eliranwong/biblematecli`
- For Web/API changes: `git clone https://github.com/eliranwong/biblemateweb`
- For data tooling: `git clone https://github.com/eliranwong/biblematedata`
