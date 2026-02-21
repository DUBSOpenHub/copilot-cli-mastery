"""Module 3: Modes — Interactive, Plan, and Autopilot."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text, box
)
from engine.quiz import Question, ScenarioQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the modes training module."""
    progress.visit_section("modes")

    while True:
        hr_fancy("🔄 Module 3: Interaction Modes", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Understand when and how to use each mode.{C.RESET}")
        print(f"  {C.DIM}The right mode at the right time = maximum productivity.{C.RESET}\n")

        result = menu([
            ("🎓 Guided Lesson: All Three Modes", "lesson"),
            ("📊 Mode Comparison Chart", "compare"),
            ("🎯 Quiz: When to Use Which Mode", "quiz"),
            ("🧩 Scenario Challenge", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson":
            _lesson(progress)
        elif result == "compare":
            _compare(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson(progress):
    hr_fancy("🎓 The Three Modes", C.BRIGHT_GREEN)
    print_difficulty("beginner")

    type_text("\n  The Copilot CLI has three interaction modes, each for different situations.", color=C.WHITE)
    pause()

    info_box(f"1️⃣  {C.GREEN}INTERACTIVE MODE{C.RESET} (Default)", f"""The standard mode — AI reads, thinks, and acts immediately.

{C.GREEN}How it works:{C.RESET}
  1. You type a prompt
  2. AI analyzes and takes action
  3. Asks for confirmation on risky operations
  4. Shows results

{C.YELLOW}Best for:{C.RESET}
  • Quick questions and explorations
  • Simple code changes
  • Running tests and builds
  • Day-to-day development tasks

{C.CYAN}Switch to it:{C.RESET} Shift+Tab (cycle until you see "Interactive")

{C.DIM}This is where most people spend 80% of their time.{C.RESET}""")
    pause()

    info_box(f"2️⃣  {C.YELLOW}PLAN MODE{C.RESET}", f"""AI creates a plan FIRST, then waits for your approval.

{C.GREEN}How it works:{C.RESET}
  1. You type a prompt
  2. AI analyzes the codebase
  3. AI presents a step-by-step plan
  4. You review and approve (or modify)
  5. AI executes the approved plan

{C.YELLOW}Best for:{C.RESET}
  • Complex refactoring across multiple files
  • Architecture changes
  • When you want to review before execution
  • Risky operations where mistakes are costly
  • Learning — see HOW the AI approaches problems

{C.CYAN}Switch to it:{C.RESET} /plan or Shift+Tab

{C.RED}Key benefit:{C.RESET} You stay in control of WHAT gets changed.""")
    pause()

    info_box(f"3️⃣  {C.MAGENTA}AUTOPILOT MODE{C.RESET} (Experimental)", f"""AI acts without asking for confirmation — full autonomy.

{C.GREEN}How it works:{C.RESET}
  1. You type a prompt
  2. AI takes action immediately
  3. No confirmation prompts
  4. Runs until task is complete

{C.RED}⚠️  IMPORTANT:{C.RESET}
  • This is an EXPERIMENTAL feature
  • Must enable with /experimental
  • Use in safe environments (version-controlled repos)
  • NOT recommended for production systems

{C.YELLOW}Best for:{C.RESET}
  • Boilerplate generation
  • Well-defined, low-risk tasks
  • When you trust the AI's judgment
  • Rapid prototyping

{C.CYAN}Related:{C.RESET} --allow-all / --yolo flags offer similar behavior""")
    pause()

    print_tip("Switch modes with Shift+Tab at any time — no need for slash commands!")
    pause()

    progress.complete_lesson("modes")
    progress.check_module_achievements()


def _compare(progress):
    hr_fancy("📊 Mode Comparison", C.BRIGHT_BLUE)
    print()

    w = 90
    header = f"  {C.BOLD}{'Feature':<25} {'Interactive':<20} {'Plan':<20} {'Autopilot':<20}{C.RESET}"
    print(header)
    print(f"  {'─' * (w - 4)}")

    rows = [
        ("Speed", "⚡ Fast", "🐢 Slower", "⚡⚡ Fastest"),
        ("Safety", "🟡 Medium", "🟢 Highest", "🔴 Lowest"),
        ("User Control", "🟡 Per-action", "🟢 Full plan review", "🔴 Minimal"),
        ("Confirmation", "Yes (risky ops)", "Yes (full plan)", "No"),
        ("Best For", "Daily tasks", "Complex changes", "Boilerplate"),
        ("Activation", "Default", "/plan, Shift+Tab", "/experimental"),
        ("Risk Level", "Medium", "Low", "High"),
        ("Learning Value", "Medium", "High (see plans)", "Low"),
    ]

    for feature, interactive, plan, autopilot in rows:
        print(f"  {C.WHITE}{feature:<25}{C.RESET} {C.GREEN}{interactive:<20}{C.RESET} {C.YELLOW}{plan:<20}{C.RESET} {C.MAGENTA}{autopilot:<20}{C.RESET}")

    print()
    print_tip("Start with Interactive, graduate to Plan for complex tasks, use Autopilot rarely.")
    pause()


def _run_quiz(progress):
    questions = [
        Question(
            "Which mode is the DEFAULT in Copilot CLI?",
            ["Plan mode", "Interactive mode", "Autopilot mode", "Safe mode"],
            1,
            "Interactive mode is the default — AI acts immediately with confirmations.",
            "beginner"
        ),
        Question(
            "In Plan mode, what happens after you type a prompt?",
            ["AI executes immediately", "AI creates a plan and waits for approval",
             "AI asks clarifying questions", "AI switches to a different model"],
            1,
            "Plan mode adds a review step — you see the plan before any changes happen.",
            "beginner"
        ),
        Question(
            "How do you quickly switch between modes?",
            ["Ctrl+M", "Shift+Tab", "/mode", "Ctrl+Tab"],
            1,
            "Shift+Tab cycles through modes: Interactive → Plan → Autopilot.",
            "beginner"
        ),
        ScenarioQuestion(
            "You need to refactor a database layer from SQL to an ORM. This will touch "
            "15+ files across models, controllers, and tests.",
            "Which mode should you use?",
            ["Interactive — just tell it what to do",
             "Plan — review the refactoring plan first",
             "Autopilot — let it handle everything",
             "Doesn't matter — any mode works"],
            1,
            "Plan mode is ideal for complex, multi-file changes. Review before execution!",
            "intermediate"
        ),
        ScenarioQuestion(
            "You're generating boilerplate CRUD endpoints for 5 new database models. "
            "The pattern is well-established and low-risk.",
            "Which mode makes sense?",
            ["Interactive with careful review",
             "Plan mode for safety",
             "Autopilot — repetitive, well-defined task",
             "Write them manually instead"],
            2,
            "Autopilot shines for repetitive, well-defined tasks with low risk.",
            "intermediate"
        ),
        Question(
            "What must you enable before using Autopilot mode?",
            ["/unsafe", "/experimental", "/allow-all", "/admin"],
            1,
            "Autopilot is experimental — enable it with /experimental first.",
            "intermediate"
        ),
        ScenarioQuestion(
            "You're exploring a new codebase and asking questions about the architecture. "
            "You're not making any changes yet.",
            "Which mode is best?",
            ["Plan mode — it's safest",
             "Interactive mode — quick Q&A",
             "Autopilot — fastest responses",
             "Any mode — no changes involved"],
            1,
            "Interactive is perfect for Q&A. Plan mode adds unnecessary overhead for read-only work.",
            "beginner"
        ),
        Question(
            "What flags provide Autopilot-like behavior from the command line?",
            ["--fast --no-confirm", "--allow-all or --yolo",
             "--auto --skip-confirm", "--unsafe --execute"],
            1,
            "--allow-all (or --yolo) skips all confirmation prompts — similar to Autopilot.",
            "advanced"
        ),
    ]
    run_quiz(questions, progress, "modes", "Interaction Modes Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "mode_selection",
        "title": "Choose the Right Mode",
        "description": "A series of real-world situations where you need to\n"
                       "pick the best interaction mode for the job.",
        "difficulty": "intermediate",
        "steps": [
            {
                "prompt": "You want to quickly check: 'What testing framework does this project use?'",
                "options": ["Plan mode", "Interactive mode", "Autopilot mode"],
                "correct": 1,
                "success_msg": "✓ Interactive is perfect for quick questions!",
                "fail_msg": "Interactive mode is ideal for quick questions with no changes.",
                "explanation": "No code changes needed, so Interactive's speed is the right choice."
            },
            {
                "prompt": "You need to migrate from Express to Fastify, touching routing, middleware, and tests.",
                "options": ["Plan mode", "Interactive mode", "Autopilot mode"],
                "correct": 0,
                "success_msg": "✓ Plan mode lets you review the migration strategy first!",
                "fail_msg": "A major migration needs Plan mode for safety and review.",
                "explanation": "Complex migrations benefit from seeing the full plan before execution."
            },
            {
                "prompt": "You're creating 10 similar React components that follow an existing pattern.",
                "options": ["Plan mode", "Interactive mode", "Autopilot mode"],
                "correct": 2,
                "success_msg": "✓ Autopilot excels at repetitive, pattern-based tasks!",
                "fail_msg": "Repetitive, low-risk, pattern-based work is Autopilot's sweet spot.",
                "explanation": "When the pattern is established and risk is low, let the AI fly."
            },
            {
                "prompt": "You're about to delete old migration files and restructure the DB schema.",
                "options": ["Plan mode", "Interactive mode", "Autopilot mode"],
                "correct": 0,
                "success_msg": "✓ Destructive operations always deserve Plan mode!",
                "fail_msg": "Any destructive operation should go through Plan mode.",
                "explanation": "Deleting files and changing schemas? You MUST review the plan first."
            },
            {
                "prompt": "You want to fix a typo in a README file.",
                "options": ["Plan mode", "Interactive mode", "Autopilot mode"],
                "correct": 1,
                "success_msg": "✓ Simple changes don't need plan review!",
                "fail_msg": "Interactive mode — a typo fix doesn't need a formal plan.",
                "explanation": "Don't over-engineer the mode choice. Simple task = simple mode."
            },
        ]
    }
    run_scenario(scenario, progress)
