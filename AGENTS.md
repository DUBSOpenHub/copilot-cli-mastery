# Agents

## Overview
Copilot CLI Mastery ships a single Copilot CLI skill (`cli-mastery`) that acts as an interactive training system. It teaches GitHub Copilot CLI through guided lessons, quizzes, scenario challenges, and a final exam across 8 modules.

## Available Skills

### cli-mastery
- **Purpose**: Interactive, in-terminal training system that takes users from beginner to CLI Wizard through 8 curriculum modules, scenario challenges, and a final exam. Tracks XP and progress via SQL across sessions.
- **Usage**:
  1. Install the skill:
     ```bash
     mkdir -p ~/.copilot/skills/cli-mastery/curriculum
     curl -sSL https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/SKILL.md \
       -o ~/.copilot/skills/cli-mastery/SKILL.md
     for f in module-1-slash-commands module-2-keyboard-shortcuts module-3-modes module-4-agents \
               module-5-skills module-6-mcp module-7-advanced module-8-configuration scenarios final-exam; do
       curl -sSL "https://raw.githubusercontent.com/DUBSOpenHub/copilot-cli-mastery/main/curriculum/${f}.md" \
         -o ~/.copilot/skills/cli-mastery/curriculum/${f}.md
     done
     ```
  2. Open Copilot CLI and say **"cliexpert"** to start.
- **Model**: Default Copilot CLI model

## Curriculum Modules

| # | Module | Topics |
|---|--------|--------|
| 1 | Slash Commands | All 42 commands across 8 categories |
| 2 | Keyboard Shortcuts | 19 shortcuts with muscle-memory training |
| 3 | Interaction Modes | Ask, Edit, Agent — when to use each |
| 4 | Agent System | Built-in agents, custom agents, orchestration |
| 5 | Skills System | What skills are, how to create and use them |
| 6 | MCP Integration | GitHub MCP server, custom servers, config |
| 7 | Advanced Techniques | Context management, prompt engineering, CI/CD |
| 8 | Configuration | Settings, themes, keybindings, permissions |

Plus **8 scenario challenges** and a **final exam**.

## Configuration
- `SKILL.md` is the slim router (≤500 tokens) that drives the skill; curriculum files are loaded on demand.
- Progress is persisted across sessions via the Copilot CLI SQL tool.
- Also installable via `/skills add DUBSOpenHub/copilot-cli-mastery` if the CLI supports remote skill installation.
