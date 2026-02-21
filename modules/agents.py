"""Module 4: Agent System — built-in and custom agents."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text,
    print_command, box
)
from engine.quiz import Question, ScenarioQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the agents training module."""
    progress.visit_section("agents")

    while True:
        hr_fancy("🤖 Module 4: Agent System", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Agents are specialized AI workers — learn to command them.{C.RESET}\n")

        result = menu([
            ("🎓 Guided Lesson: Built-in Agents", "lesson_builtin"),
            ("🎓 Guided Lesson: Custom Agents", "lesson_custom"),
            ("🎓 Guided Lesson: Agent Profiles & /agent", "lesson_profiles"),
            ("🎯 Quiz: Agent Mastery", "quiz"),
            ("🧩 Scenario: Agent Orchestration", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson_builtin":
            _lesson_builtin(progress)
        elif result == "lesson_custom":
            _lesson_custom(progress)
        elif result == "lesson_profiles":
            _lesson_profiles(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson_builtin(progress):
    hr_fancy("🎓 Built-in Agents", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Four specialized agents, each with a unique purpose.", color=C.WHITE)
    pause()

    info_box(f"🔍 {C.CYAN}explore{C.RESET} — Fast Codebase Q&A", f"""A lightweight agent optimized for speed using Haiku model.

{C.GREEN}Best for:{C.RESET}
  • "What does this function do?"
  • "Where is authentication implemented?"
  • "Find all API endpoints"
  • Quick codebase exploration

{C.YELLOW}Capabilities:{C.RESET} grep, glob, view (read-only tools)
{C.CYAN}Model:{C.RESET} Haiku (fast, cheap)
{C.RED}Cannot:{C.RESET} Make changes, run commands

{C.DIM}Returns focused answers under 300 words.
Safe to run multiple in parallel!{C.RESET}""")
    pause()

    info_box(f"⚡ {C.YELLOW}task{C.RESET} — Command Executor", f"""Runs commands and reports results concisely.

{C.GREEN}Best for:{C.RESET}
  • Running test suites
  • Building projects
  • Linting code
  • Installing dependencies

{C.YELLOW}Output behavior:{C.RESET}
  • Success → brief summary ("All 247 tests passed")
  • Failure → full output (stack traces, errors)

{C.CYAN}Model:{C.RESET} Haiku (fast)
{C.RED}Pro tip:{C.RESET} Keeps main context clean by minimizing output.""")
    pause()

    info_box(f"🧠 {C.GREEN}general-purpose{C.RESET} — Full Capability", f"""The most capable agent — runs in a separate context window.

{C.GREEN}Best for:{C.RESET}
  • Complex multi-step tasks
  • Tasks requiring the complete toolset
  • Work that needs high-quality reasoning
  • Independent sub-projects

{C.YELLOW}Capabilities:{C.RESET} ALL tools (edit, create, bash, etc.)
{C.CYAN}Model:{C.RESET} Sonnet (balanced power and speed)

{C.DIM}Runs in a subprocess to keep your main conversation clean.{C.RESET}""")
    pause()

    info_box(f"📝 {C.MAGENTA}code-review{C.RESET} — Review Specialist", f"""Analyzes code changes with extremely high signal-to-noise ratio.

{C.GREEN}Analyzes:{C.RESET}
  • Staged/unstaged changes
  • Branch diffs
  • PR changes

{C.YELLOW}Only flags things that matter:{C.RESET}
  ✅ Bugs, security vulnerabilities, logic errors
  ❌ Never comments on style, formatting, or trivial matters

{C.RED}Important:{C.RESET} Will NOT modify code — read-only analysis.

{C.CYAN}Model:{C.RESET} Uses all CLI tools for investigation.""")
    pause()

    progress.complete_lesson("agents_builtin")
    progress.check_module_achievements()


def _lesson_custom(progress):
    hr_fancy("🎓 Custom Agents", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Create your own specialized agents for any workflow.", color=C.WHITE)
    pause()

    info_box("📂 Agent File Locations", f"""Custom agents can be defined at three levels:

{C.GREEN}1. Personal (user-level):{C.RESET}
   ~/.copilot/agents/*.md
   → Available in ALL your projects

{C.GREEN}2. Project-level:{C.RESET}
   .github/agents/*.md
   → Available to everyone in this repo

{C.GREEN}3. Organization-level:{C.RESET}
   Configured at the org level
   → Available to all org members

{C.YELLOW}File format:{C.RESET} Markdown (.md) files with agent configuration""")
    pause()

    info_box("📝 Agent File Structure", f"""An agent file is a Markdown document with YAML frontmatter:

{C.GREEN}Example: .github/agents/db-expert.md{C.RESET}

```
---
name: db-expert
description: Database migration and schema expert
tools: [bash, edit, create, view, grep, glob]
model: claude-sonnet-4.5
---

You are a database expert specializing in:
- Schema design and migrations
- Query optimization
- Index strategy
- Data integrity

Always check existing migrations before creating new ones.
Run tests after any schema change.
```

{C.YELLOW}Key fields:{C.RESET}
  • name: identifier for /agent command
  • description: shown in agent list
  • tools: which tools the agent can use
  • model: which AI model to use""")
    pause()

    info_box("🔧 Agent Configuration Tips", f"""{C.GREEN}Give agents clear boundaries:{C.RESET}
  • Specify exactly what tools they need
  • Define their expertise area
  • Include workflow instructions
  • Set the right model for the job

{C.YELLOW}Model selection:{C.RESET}
  • Haiku: fast, simple agents (linting, searching)
  • Sonnet: balanced agents (most custom agents)
  • Opus: complex reasoning agents (architecture)

{C.CYAN}Pro tips:{C.RESET}
  • Keep agent instructions focused and specific
  • Test with different models to find the sweet spot
  • Use /agent to verify your agent is discovered""")
    pause()

    progress.complete_lesson("agents_custom")
    progress.check_module_achievements()


def _lesson_profiles(progress):
    hr_fancy("🎓 Agent Profiles & /agent Command", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    info_box("The /agent Command", f"""{C.GREEN}/agent{C.RESET}              — List all available agents
{C.GREEN}/agent explore{C.RESET}     — Switch to the explore agent
{C.GREEN}/agent task{C.RESET}        — Switch to the task agent
{C.GREEN}/agent my-custom{C.RESET}   — Switch to a custom agent

{C.YELLOW}What you'll see:{C.RESET}
  • Agent name and description
  • Available tools
  • Model being used
  • Source (built-in, user, project, org)""")
    pause()

    info_box("Agent Orchestration Patterns", f"""{C.GREEN}Pattern 1: Explore then Execute{C.RESET}
  1. Use 'explore' to understand the codebase
  2. Switch to 'general-purpose' for changes
  3. Use 'code-review' to verify

{C.GREEN}Pattern 2: Parallel Exploration{C.RESET}
  Launch multiple 'explore' agents simultaneously
  to answer different questions in parallel

{C.GREEN}Pattern 3: Specialist Handoff{C.RESET}
  1. Main conversation identifies the task
  2. /delegate to a custom specialist agent
  3. Agent works independently
  4. Review results with /fleet or /tasks

{C.YELLOW}Remember:{C.RESET} explore agents are safe to parallelize;
task and general-purpose agents have side effects.""")
    pause()

    progress.complete_lesson("agents_profiles")
    progress.complete_lesson("agents")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "Which built-in agent is best for quickly answering 'where is X in the codebase?'",
            ["task", "general-purpose", "explore", "code-review"],
            2,
            "explore is optimized for fast codebase Q&A using Haiku.",
            "beginner"
        ),
        Question(
            "Which agent should you use to run a test suite?",
            ["explore", "task", "general-purpose", "code-review"],
            1,
            "task agent runs commands and gives concise success/failure reports.",
            "beginner"
        ),
        Question(
            "Where do you put agent files for personal use across all projects?",
            [".github/agents/", "~/.copilot/agents/", "/etc/copilot/agents/", "~/.config/agents/"],
            1,
            "~/.copilot/agents/ is for user-level agents available everywhere.",
            "intermediate"
        ),
        Question(
            "Which agent will NEVER modify your code?",
            ["explore", "task", "code-review", "Both explore and code-review"],
            3,
            "Both explore (read-only) and code-review (analysis only) won't modify code.",
            "intermediate"
        ),
        Question(
            "What model does the explore agent use by default?",
            ["Opus", "Sonnet", "Haiku", "GPT-4"],
            2,
            "Haiku is fast and cheap — perfect for quick exploration queries.",
            "intermediate"
        ),
        ScenarioQuestion(
            "You're working on a large codebase. You need to understand the auth system, "
            "the database layer, and the API routing — all at the same time.",
            "What's the most efficient approach?",
            ["Ask about each one sequentially in Interactive mode",
             "Launch multiple explore agents in parallel",
             "Use the general-purpose agent for everything",
             "Read the docs manually"],
            1,
            "explore agents can safely run in parallel — query all three simultaneously!",
            "advanced"
        ),
        ScenarioQuestion(
            "You need a custom agent that analyzes Terraform files, checks for security "
            "misconfigurations, and suggests fixes. It should be available to your whole team.",
            "Where should you create this agent?",
            ["~/.copilot/agents/terraform-sec.md",
             ".github/agents/terraform-sec.md",
             "terraform-sec.md in repo root",
             "/etc/copilot/agents/terraform-sec.md"],
            1,
            ".github/agents/ makes it available to everyone working on the repo.",
            "advanced"
        ),
    ]
    run_quiz(questions, progress, "agents", "Agent System Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "agent_orchestration",
        "title": "Agent Orchestration Challenge",
        "description": "You're leading a complex project. Use the right agents\n"
                       "at each step to maximize efficiency.",
        "difficulty": "advanced",
        "steps": [
            {
                "prompt": "First, you need to understand the existing code architecture. Which agent?",
                "options": ["general-purpose", "explore", "task", "code-review"],
                "correct": 1,
                "success_msg": "✓ explore is perfect for fast codebase understanding!",
                "fail_msg": "explore is the right choice for quick codebase Q&A.",
                "explanation": "Start with explore to build understanding before making changes."
            },
            {
                "prompt": "Now you need to run the existing test suite to establish a baseline. Which agent?",
                "options": ["explore", "task", "general-purpose", "code-review"],
                "correct": 1,
                "success_msg": "✓ task runs commands and reports results cleanly!",
                "fail_msg": "task is designed for running commands like test suites.",
                "explanation": "task gives brief success summaries and full failure details."
            },
            {
                "prompt": "Time for a major refactoring that will touch 20+ files. Which agent?",
                "options": ["explore", "task", "general-purpose", "code-review"],
                "correct": 2,
                "success_msg": "✓ general-purpose has full capability for complex changes!",
                "fail_msg": "general-purpose has all tools needed for major refactoring.",
                "explanation": "Complex multi-file changes need the full toolset of general-purpose."
            },
            {
                "prompt": "After the refactoring, you want an AI review of all changes. Which agent?",
                "options": ["explore", "task", "general-purpose", "code-review"],
                "correct": 3,
                "success_msg": "✓ code-review specializes in high-signal change analysis!",
                "fail_msg": "code-review analyzes changes and only flags what matters.",
                "explanation": "code-review won't nit-pick style — it focuses on real issues."
            },
        ]
    }
    run_scenario(scenario, progress)
