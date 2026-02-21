"""Module 7: Advanced Techniques — power user workflows."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text,
    print_command, box, print_warning
)
from engine.quiz import Question, ScenarioQuestion, FillInQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the advanced techniques training module."""
    progress.visit_section("advanced")

    while True:
        hr_fancy("🚀 Module 7: Advanced Techniques", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Master the techniques that separate beginners from experts.{C.RESET}\n")

        result = menu([
            ("🎓 Context & File Management", "lesson_context"),
            ("🎓 Custom Instructions Deep-Dive", "lesson_instructions"),
            ("🎓 Session Continuity & Workflow", "lesson_session"),
            ("🎓 Code Review & Security", "lesson_review"),
            ("🎓 Pro Tips & Hidden Features", "lesson_pro"),
            ("🎯 Expert Quiz", "quiz"),
            ("🧩 Advanced Scenario", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson_context":
            _lesson_context(progress)
        elif result == "lesson_instructions":
            _lesson_instructions(progress)
        elif result == "lesson_session":
            _lesson_session(progress)
        elif result == "lesson_review":
            _lesson_review(progress)
        elif result == "lesson_pro":
            _lesson_pro(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson_context(progress):
    hr_fancy("🎓 Context & File Management", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Context management is the #1 skill that separates experts from beginners.", color=C.WHITE)
    pause()

    info_box("@ File Mentions — Deep Dive", f"""File mentions are your primary context injection tool.

{C.GREEN}Syntax:{C.RESET}
  @filename.ext          — single file
  @path/to/file.ts       — file with path
  @src/components/       — directory (lists contents)

{C.YELLOW}Power patterns:{C.RESET}
  "Fix @src/auth.ts to match @tests/auth.test.ts"
    → AI sees both files, understands the relationship

  "Refactor @src/api/ following patterns in @src/utils/helpers.ts"
    → AI sees directory structure AND a pattern file

{C.RED}Context budget:{C.RESET}
  Every @ mention uses context tokens. Be selective!
  Large files consume a LOT of context.

{C.CYAN}Strategy:{C.RESET}
  • Mention specific files, not directories when possible
  • Use /context to monitor token usage
  • Use /compact when context fills up""")
    pause()

    info_box("/context — Token Visualization", f"""Understanding your context window is critical.

{C.GREEN}/context{C.RESET} shows:
  • Total tokens used / available
  • Breakdown by category:
    - System instructions
    - Conversation history
    - File contents
    - Tool results

{C.YELLOW}When to check:{C.RESET}
  • Before adding large files
  • When AI seems to forget earlier context
  • After a long conversation
  • Before using /compact

{C.RED}Warning signs:{C.RESET}
  • Token usage > 80% — consider /compact
  • Token usage > 95% — /compact immediately
  • AI contradicting earlier statements""")
    pause()

    progress.complete_lesson("adv_context")


def _lesson_instructions(progress):
    hr_fancy("🎓 Custom Instructions Deep-Dive", C.BRIGHT_GREEN)
    print_difficulty("expert")

    type_text("\n  Shape the AI's behavior with custom instruction files.", color=C.WHITE)
    pause()

    info_box("Instruction File Hierarchy", f"""Multiple instruction files loaded in order of specificity:

{C.GREEN}1. Global (user-level):{C.RESET}
   ~/.copilot/copilot-instructions.md
   → Applies to ALL your projects

{C.GREEN}2. Repository-level:{C.RESET}
   .github/copilot-instructions.md
   → Applies to this repo for all users

{C.GREEN}3. Model-specific:{C.RESET}
   CLAUDE.md  — instructions for Claude models
   GEMINI.md  — instructions for Gemini models
   → Loaded based on active model

{C.GREEN}4. Agent instructions:{C.RESET}
   AGENTS.md  — instructions for agent behavior
   → Loaded when using agents

{C.GREEN}5. Path-specific:{C.RESET}
   .github/instructions/*.instructions.md
   → Loaded based on file path matching

{C.YELLOW}Loading order:{C.RESET}
   Global → Repo → Model → Agent → Path-specific
   More specific instructions override general ones.""")
    pause()

    info_box("Writing Effective Instructions", f"""{C.GREEN}What to include:{C.RESET}
  • Coding standards and conventions
  • Architecture patterns to follow
  • Testing requirements
  • Forbidden patterns or approaches
  • Domain-specific context

{C.YELLOW}Example CLAUDE.md:{C.RESET}
```markdown
# Project Instructions

## Code Style
- Use TypeScript strict mode
- Prefer functional components with hooks
- Always use named exports

## Testing
- Write tests for all new functions
- Use React Testing Library, not Enzyme
- Minimum 80% coverage for new code

## Architecture
- Follow the repository pattern for data access
- Use Zod for input validation
- Never use `any` type
```

{C.RED}Anti-patterns:{C.RESET}
  • Instructions that are too vague
  • Contradicting instructions across files
  • Very long instruction files (wastes context)""")
    pause()

    info_box("Path-Specific Instructions", f"""Target instructions to specific parts of your codebase.

{C.GREEN}Location:{C.RESET} .github/instructions/

{C.YELLOW}Examples:{C.RESET}
  .github/instructions/api.instructions.md
  → Loaded when working on API-related files

  .github/instructions/frontend.instructions.md
  → Loaded when working on frontend code

{C.CYAN}Pattern matching:{C.RESET}
  Instructions file names can match patterns.
  The AI loads relevant instructions based on
  which files you're working with.

{C.GREEN}Use case:{C.RESET}
  Different coding standards for different parts
  of a monorepo — frontend vs. backend vs. infra.""")
    pause()

    progress.complete_lesson("adv_instructions")


def _lesson_session(progress):
    hr_fancy("🎓 Session Continuity & Workflow", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Never lose your work — master session management.", color=C.WHITE)
    pause()

    info_box("Session Continuity", f"""{C.GREEN}/resume{C.RESET}           — resume a previous session
{C.GREEN}--continue{C.RESET}        — CLI flag to resume last session

{C.YELLOW}Session workflow:{C.RESET}
  1. Start working → session auto-created
  2. /rename "auth refactor" → name it
  3. Exit when done → auto-saved
  4. Next day: copilot --continue
  5. Or: /resume → pick from session list

{C.CYAN}What's preserved:{C.RESET}
  • Conversation history
  • File context
  • Current working directory
  • Session name and metadata

{C.RED}What's NOT preserved:{C.RESET}
  • Running processes
  • Environment variables set during session
  • MCP server connections (reconnected on resume)""")
    pause()

    info_box("/compact — Context Management", f"""When your context is filling up, /compact saves the day.

{C.GREEN}What it does:{C.RESET}
  1. AI summarizes the entire conversation
  2. Old messages replaced with the summary
  3. Key facts and decisions are preserved
  4. Context space is freed for new work

{C.YELLOW}When to use:{C.RESET}
  • After completing a sub-task
  • When AI starts forgetting earlier context
  • When /context shows > 80% usage
  • Before starting a new phase of work

{C.RED}Strategy:{C.RESET}
  Don't wait until context is full!
  /compact proactively at natural breakpoints.""")
    pause()

    info_box("! Shell Bypass — Advanced Usage", f"""The ! prefix is more powerful than you think.

{C.GREEN}Basic usage:{C.RESET}
  !git status, !npm test, !ls -la

{C.YELLOW}Advanced patterns:{C.RESET}
  !git log --oneline -10
    → Quick history check

  !find . -name "*.test.ts" | head -20
    → Find test files

  !cat .env.example
    → Check env template

  !docker compose ps
    → Check running services

{C.CYAN}Key insight:{C.RESET}
  Shell bypass output is visible to the AI!
  Use it to quickly add information to context
  without the overhead of the tool system.""")
    pause()

    progress.complete_lesson("adv_session")


def _lesson_review(progress):
    hr_fancy("🎓 Code Review & Security", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Use AI to catch bugs before they reach production.", color=C.WHITE)
    pause()

    info_box("/review — AI Code Review", f"""{C.GREEN}Usage:{C.RESET}
  /review              — review staged changes
  /review --diff main  — review changes vs. main branch
  /review              — review unstaged changes

{C.YELLOW}What it focuses on:{C.RESET}
  ✅ Bugs and logic errors
  ✅ Security vulnerabilities
  ✅ Race conditions
  ✅ Error handling gaps
  ✅ Performance issues

  ❌ Does NOT comment on style
  ❌ Does NOT nitpick formatting
  ❌ Does NOT flag trivial issues

{C.CYAN}Workflow:{C.RESET}
  1. Make your changes
  2. git add . (stage them)
  3. /review
  4. Fix any flagged issues
  5. git commit""")
    pause()

    info_box("Ctrl+T — Reasoning Toggle", f"""Toggle the AI's chain-of-thought visibility.

{C.GREEN}When to enable:{C.RESET}
  • Debugging unexpected AI behavior
  • Learning how the AI approaches problems
  • Verifying logic before accepting changes
  • Understanding why the AI chose an approach

{C.YELLOW}When to disable:{C.RESET}
  • For cleaner, faster output
  • When you trust the AI's approach
  • During routine tasks

{C.CYAN}Pro tip:{C.RESET}
  Enable reasoning for complex tasks, then turn it off
  once you're confident in the approach.""")
    pause()

    info_box("--allow-all / --yolo Flags", f"""Skip all confirmation prompts from the command line.

{C.GREEN}Usage:{C.RESET}
  copilot --allow-all    — skip confirmations
  copilot --yolo         — same thing, shorter

{C.RED}⚠️ Warning:{C.RESET}
  This means the AI can:
  • Edit any file without asking
  • Run any command without asking
  • Delete files without asking

{C.YELLOW}When it's OK:{C.RESET}
  • In a Docker container / sandbox
  • On a branch you can throw away
  • For well-defined, low-risk tasks
  • When you have good backups (git)

{C.RED}When it's NOT OK:{C.RESET}
  • On production branches
  • With sensitive data access
  • For untested workflows""")
    pause()

    progress.complete_lesson("adv_review")


def _lesson_pro(progress):
    hr_fancy("🎓 Pro Tips & Hidden Features", C.BRIGHT_GREEN)
    print_difficulty("expert")

    type_text("\n  The secrets that CLI wizards know.", color=C.WHITE)
    pause()

    info_box("/delegate — Coding Agent Handoff", f"""Hand off complex tasks to a dedicated coding agent.

{C.GREEN}Usage:{C.RESET}
  /delegate "refactor the auth module to use JWT tokens"
  /delegate "add comprehensive error handling to the API"

{C.YELLOW}How it works:{C.RESET}
  1. A new agent is spawned in a separate context
  2. It gets the full toolset (edit, create, bash, etc.)
  3. It works independently on your task
  4. You can monitor with /fleet or /tasks
  5. Results are reported back

{C.CYAN}Best for:{C.RESET}
  • Tasks that are well-defined but large
  • Work you don't need to supervise step-by-step
  • Parallel workstreams""")
    pause()

    info_box("LSP Configuration", f"""Language Server Protocol gives the AI code intelligence.

{C.GREEN}Configuration files:{C.RESET}
  • lsp-config.json  (user-level)
  • .github/lsp.json (project-level)

{C.YELLOW}What LSP provides:{C.RESET}
  • Go-to-definition
  • Find references
  • Symbol search
  • Type information
  • Diagnostics (errors, warnings)

{C.CYAN}The /lsp command:{C.RESET}
  • /lsp — view LSP configuration status
  • Configure language servers for your project
  • AI uses LSP for more accurate code navigation

{C.GREEN}Pro tip:{C.RESET}
  A properly configured LSP dramatically improves
  the AI's ability to understand and navigate code.""")
    pause()

    info_box("Expert Workflow Patterns", f"""{C.GREEN}Pattern 1: Morning Startup{C.RESET}
  copilot --continue
  !git pull
  !git log --oneline -5
  "What's changed since yesterday?"

{C.GREEN}Pattern 2: Feature Development{C.RESET}
  1. Start in Interactive: explore codebase
  2. Switch to Plan mode (Shift+Tab) for implementation
  3. Use /delegate for large sub-tasks
  4. Run /review before committing
  5. /compact between phases

{C.GREEN}Pattern 3: Debugging{C.RESET}
  1. Enable reasoning: Ctrl+T
  2. Provide context: @error-file.ts @test-file.ts
  3. "Debug the failing test in @tests/auth.test.ts"
  4. Check with: !npm test

{C.GREEN}Pattern 4: Codebase Learning{C.RESET}
  1. Use explore agents for fast Q&A
  2. "Explain the architecture of @src/"
  3. "@README.md @CONTRIBUTING.md summarize setup"
  4. "What patterns does @src/api/ use?"

{C.GREEN}Pattern 5: End of Day{C.RESET}
  /rename "feature: user-auth-jwt"
  !git stash (or commit)
  /exit""")
    pause()

    progress.complete_lesson("adv_pro")
    progress.complete_lesson("advanced")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "Which instruction file is loaded for ALL your projects?",
            ["CLAUDE.md", ".github/copilot-instructions.md",
             "~/.copilot/copilot-instructions.md", "AGENTS.md"],
            2,
            "The global instruction file in ~/.copilot/ applies everywhere.",
            "intermediate"
        ),
        Question(
            "When should you use /compact?",
            ["When the AI is too verbose", "When context token usage is high",
             "To minimize code", "To compress files"],
            1,
            "/compact summarizes conversation to free context space. Use at natural breakpoints.",
            "intermediate"
        ),
        Question(
            "What does Ctrl+T toggle?",
            ["Terminal theme", "Token counter", "AI reasoning display", "Tab width"],
            2,
            "Ctrl+T shows/hides the AI's chain-of-thought reasoning process.",
            "intermediate"
        ),
        Question(
            "What's the --yolo flag equivalent to?",
            ["/experimental", "--allow-all (skip all confirmations)",
             "--fast (use fastest model)", "--debug"],
            1,
            "--yolo = --allow-all. Both skip tool call confirmations.",
            "advanced"
        ),
        Question(
            "Where are path-specific instructions stored?",
            [".github/instructions/*.instructions.md", "~/.copilot/paths/",
             ".instructions/", "src/.instructions"],
            0,
            "Path-specific instructions in .github/instructions/ are loaded by file path matching.",
            "advanced"
        ),
        Question(
            "What does /delegate do?",
            ["Delegates permissions", "Hands off a task to a dedicated coding agent",
             "Delegates to another user", "Forwards to IDE"],
            1,
            "/delegate spawns an independent agent for complex tasks.",
            "intermediate"
        ),
        FillInQuestion(
            "What CLI flag resumes your last session? (e.g., copilot ???)",
            ["--continue"],
            "copilot --continue resumes the last session.",
            "intermediate", "Think about what you want to do — keep going."
        ),
        ScenarioQuestion(
            "You're working on a monorepo with a Python backend, React frontend, "
            "and Terraform infra. Each has different coding standards.",
            "What's the best way to handle different instructions?",
            [
                "One big CLAUDE.md with all rules",
                "Path-specific instructions in .github/instructions/",
                "Mention the standards in every prompt",
                "Different branches for each standard"
            ],
            1,
            "Path-specific instructions let you have different rules for different code paths.",
            "expert"
        ),
        ScenarioQuestion(
            "Your context is at 90% capacity. You've completed the auth module "
            "and are about to start the payment module.",
            "What should you do?",
            [
                "Start a new session",
                "Use /compact to summarize, then continue",
                "Just keep going",
                "Copy important notes elsewhere"
            ],
            1,
            "/compact at natural task boundaries preserves key context while freeing space.",
            "advanced"
        ),
        Question(
            "What files configure LSP in a project?",
            ["lsp-config.json and .github/lsp.json", "tsconfig.json",
             ".lsp/config.yaml", "language-server.json"],
            0,
            "LSP is configured in lsp-config.json (user) or .github/lsp.json (project).",
            "expert"
        ),
    ]
    run_quiz(questions, progress, "advanced", "Advanced Techniques Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "expert_workflow",
        "title": "Expert Daily Workflow",
        "description": "You're starting a complex feature. Walk through\n"
                       "the optimal workflow using advanced techniques.",
        "difficulty": "expert",
        "steps": [
            {
                "prompt": "Starting your day, you want to continue from yesterday's session. How?",
                "options": [
                    "Start fresh and re-explain everything",
                    "copilot --continue",
                    "Copy yesterday's conversation",
                    "Read the session log file manually"
                ],
                "correct": 1,
                "success_msg": "✓ --continue seamlessly resumes your last session!",
                "fail_msg": "copilot --continue resumes the last session with full context.",
                "explanation": "Session continuity saves time and preserves context."
            },
            {
                "prompt": "You need to understand a complex module before changing it. Best approach?",
                "options": [
                    "Read all the source files manually",
                    "Ask the AI in Interactive mode with @ file mentions",
                    "Run the tests and hope for the best",
                    "Start changing code and see what breaks"
                ],
                "correct": 1,
                "success_msg": "✓ @ mentions give the AI exactly the right context!",
                "fail_msg": "Use @ mentions to give the AI targeted context for understanding.",
                "explanation": "@ file mentions are the fastest way to build AI context."
            },
            {
                "prompt": "You're ready to implement a complex refactoring. Which mode?",
                "options": [
                    "Stay in Interactive mode",
                    "Switch to Plan mode with Shift+Tab",
                    "Use Autopilot for speed",
                    "Use /delegate immediately"
                ],
                "correct": 1,
                "success_msg": "✓ Plan mode for complex changes — review before execution!",
                "fail_msg": "Complex refactoring deserves Plan mode for review.",
                "explanation": "Shift+Tab to Plan mode lets you review the approach first."
            },
            {
                "prompt": "Mid-session, context is at 85%. You've finished phase 1 of 3. What now?",
                "options": [
                    "Start a new session for phase 2",
                    "/compact to summarize phase 1, then continue",
                    "Hope context doesn't run out",
                    "/clear and start fresh"
                ],
                "correct": 1,
                "success_msg": "✓ /compact at natural breakpoints is expert-level context management!",
                "fail_msg": "/compact preserves key context while freeing up space.",
                "explanation": "Don't wait until context runs out. Compact proactively."
            },
            {
                "prompt": "Before committing, you want AI review of your changes. What command?",
                "options": ["/diff", "/review", "/check", "Just commit"],
                "correct": 1,
                "success_msg": "✓ /review catches bugs, security issues, and logic errors!",
                "fail_msg": "/review provides high-signal code review of your changes.",
                "explanation": "Always /review before committing. It catches real issues."
            },
        ]
    }
    run_scenario(scenario, progress)
