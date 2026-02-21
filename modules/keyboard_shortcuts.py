"""Module 2: Keyboard Shortcuts — complete training."""

from engine.ui import (
    C, hr_fancy, print_shortcut, print_tip, pause,
    info_box, menu, hr, print_difficulty, type_text
)
from engine.quiz import Question, FillInQuestion, ScenarioQuestion, run_quiz, run_scenario


SHORTCUTS = {
    "📝 Input & Editing": [
        ("↑ / ↓", "Navigate command history (previous/next)"),
        ("Ctrl+A", "Move cursor to beginning of line"),
        ("Ctrl+E", "Move cursor to end of line"),
        ("Meta+← / Meta+→", "Move cursor by word (Option+Arrow on Mac)"),
        ("Ctrl+H", "Delete character before cursor (like Backspace)"),
        ("Ctrl+W", "Delete word before cursor"),
        ("Ctrl+U", "Delete from cursor to beginning of line"),
        ("Ctrl+K", "Delete from cursor to end of line"),
        ("Ctrl+X → Ctrl+E", "Open current input in $EDITOR for multi-line editing"),
    ],
    "🚀 Execution & Control": [
        ("Enter", "Submit prompt / execute command"),
        ("Ctrl+S", "Run command, preserving input in the prompt"),
        ("Esc", "Cancel current operation / dismiss"),
        ("Ctrl+C", "Cancel running operation / clear line / exit (triple press)"),
        ("Ctrl+D", "Shutdown the CLI (EOF signal)"),
    ],
    "🔄 Mode & Display": [
        ("Shift+Tab", "Cycle through modes: Interactive → Plan → (Autopilot)"),
        ("Ctrl+T", "Toggle reasoning/thinking display on or off"),
        ("Ctrl+O", "Expand recent timeline entry"),
        ("Ctrl+E", "Expand all timeline entries (in timeline context)"),
        ("Ctrl+L", "Clear the terminal screen"),
    ],
    "📎 Special Input": [
        ("@ + filename", "Mention a file to add it to context (e.g., @src/app.ts)"),
        ("! + command", "Shell bypass — run a shell command directly (e.g., !ls -la)"),
    ],
}


def run_lesson(progress):
    """Run the keyboard shortcuts training module."""
    progress.visit_section("keyboard_shortcuts")

    while True:
        hr_fancy("⌨️  Module 2: Keyboard Shortcuts", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Master every keyboard shortcut for lightning-fast CLI usage.{C.RESET}")
        print(f"  {C.DIM}20+ shortcuts organized by function.{C.RESET}\n")

        result = menu([
            ("📚 Browse All Shortcuts (Reference)", "browse"),
            ("🎓 Guided Lesson: Essential Shortcuts", "lesson_essential"),
            ("🎓 Guided Lesson: Advanced Shortcuts", "lesson_advanced"),
            ("🎓 Guided Lesson: Special Input Tricks", "lesson_special"),
            ("🎯 Quiz: Test Your Knowledge", "quiz"),
            ("🧩 Scenario Challenge", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "browse":
            _browse_shortcuts(progress)
        elif result == "lesson_essential":
            _lesson_essential(progress)
        elif result == "lesson_advanced":
            _lesson_advanced(progress)
        elif result == "lesson_special":
            _lesson_special(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _browse_shortcuts(progress):
    while True:
        hr_fancy("📚 Shortcut Reference", C.BRIGHT_BLUE)
        categories = list(SHORTCUTS.keys())
        result = menu([(cat, cat) for cat in categories], "Select category")

        if result is None:
            return

        print()
        hr_fancy(result, C.BRIGHT_BLUE)
        print()
        for keys, desc in SHORTCUTS[result]:
            print_shortcut(keys, desc)
        print()
        pause()


def _lesson_essential(progress):
    hr_fancy("🎓 Essential Shortcuts", C.BRIGHT_GREEN)
    print_difficulty("beginner")

    type_text("\n  These shortcuts will save you hours every week.", color=C.WHITE)
    pause()

    info_box("1️⃣  Ctrl+C — The Universal Stop Button", f"""The most important shortcut — stops what's happening.

{C.GREEN}Single press:{C.RESET}  Cancel current AI operation
{C.GREEN}Double press:{C.RESET}  Clear the current line
{C.GREEN}Triple press:{C.RESET}  Exit the CLI entirely

{C.YELLOW}Also:{C.RESET} Ctrl+D sends EOF signal to shutdown immediately.""")
    pause()

    info_box("2️⃣  ↑ / ↓ — Command History", f"""Navigate through your previous commands and prompts.

{C.GREEN}↑ (Up Arrow):{C.RESET}    Previous command
{C.GREEN}↓ (Down Arrow):{C.RESET}  Next command

{C.YELLOW}Pro tip:{C.RESET} Start typing, then press ↑ to search history
for commands starting with what you've typed.""")
    pause()

    info_box("3️⃣  Shift+Tab — Cycle Modes", f"""Quickly switch between interaction modes:

  {C.GREEN}Interactive{C.RESET} → {C.YELLOW}Plan{C.RESET} → {C.MAGENTA}Autopilot*{C.RESET} → {C.GREEN}Interactive{C.RESET}

{C.GREEN}Interactive:{C.RESET}  AI acts immediately (default)
{C.YELLOW}Plan:{C.RESET}         AI proposes a plan, you approve
{C.MAGENTA}Autopilot:{C.RESET}    AI acts without confirmation (experimental)

{C.DIM}*Autopilot requires /experimental to be enabled{C.RESET}""")
    pause()

    info_box("4️⃣  Ctrl+L — Clear Screen", f"""Clears the terminal screen instantly.

Same as the /clear slash command, but faster!

{C.YELLOW}Pro tip:{C.RESET} Use this when your terminal gets cluttered
with output from builds, tests, or long conversations.""")
    pause()

    info_box("5️⃣  Esc — Cancel / Dismiss", f"""Cancel the current operation or dismiss a prompt.

{C.GREEN}During AI response:{C.RESET}  Stops generation
{C.GREEN}During input:{C.RESET}       Clears current input
{C.GREEN}During prompt:{C.RESET}      Dismisses the prompt

Lighter than Ctrl+C — just cancels, doesn't clear.""")
    pause()

    progress.complete_lesson("keys_essential")
    progress.complete_lesson("keys_1")
    progress.complete_lesson("keys_2")
    progress.complete_lesson("keys_3")
    progress.complete_lesson("keys_4")
    progress.complete_lesson("keys_5")
    progress.check_module_achievements()


def _lesson_advanced(progress):
    hr_fancy("🎓 Advanced Shortcuts", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Unlock the hidden power of the terminal.", color=C.WHITE)
    pause()

    info_box("1️⃣  Ctrl+S — Run, Keep Input", f"""Submits your prompt but KEEPS the text in the input line.

{C.GREEN}Why:{C.RESET} Perfect for iterating on a prompt!
  1. Type a prompt
  2. Press Ctrl+S to run it
  3. Edit the prompt slightly
  4. Press Ctrl+S again

{C.YELLOW}Use case:{C.RESET} Testing different prompt phrasings
without retyping from scratch.""")
    pause()

    info_box("2️⃣  Ctrl+T — Toggle Reasoning", f"""Show or hide the AI's reasoning/thinking process.

{C.GREEN}When ON:{C.RESET}   You see the AI's chain of thought
{C.GREEN}When OFF:{C.RESET}  Just the final answer (cleaner output)

{C.YELLOW}Pro tip:{C.RESET} Turn it ON when:
  • Debugging unexpected AI behavior
  • Learning how the AI approaches problems
  • Verifying the AI's logic before accepting

Turn it OFF for faster, cleaner output.""")
    pause()

    info_box("3️⃣  Ctrl+O / Ctrl+E — Timeline Navigation", f"""{C.GREEN}Ctrl+O:{C.RESET}  Expand the most recent timeline entry
{C.GREEN}Ctrl+E:{C.RESET}  Expand ALL timeline entries

The timeline shows:
  • File operations (reads, edits, creates)
  • Command executions (bash, tests, builds)
  • Tool calls and their results

{C.YELLOW}Note:{C.RESET} Ctrl+E also moves cursor to end of line
in regular editing context.""")
    pause()

    info_box("4️⃣  Ctrl+X → Ctrl+E — Edit in $EDITOR", f"""Opens your current input in your configured $EDITOR.

{C.GREEN}Steps:{C.RESET}
  1. Press Ctrl+X, then Ctrl+E
  2. Your text editor opens with current input
  3. Write/edit your prompt with full editor power
  4. Save and close to submit

{C.YELLOW}Perfect for:{C.RESET}
  • Multi-line prompts
  • Complex instructions
  • Pasting code snippets

Set your editor: export EDITOR=vim  (or nano, code, etc.)""")
    pause()

    info_box("5️⃣  Line Editing Shortcuts", f"""Standard readline shortcuts that work in the CLI:

{C.GREEN}Ctrl+A{C.RESET}        Move to beginning of line
{C.GREEN}Ctrl+E{C.RESET}        Move to end of line
{C.GREEN}Meta+← / →{C.RESET}   Move by word (Option+Arrow on Mac)
{C.GREEN}Ctrl+H{C.RESET}        Delete char before cursor
{C.GREEN}Ctrl+W{C.RESET}        Delete word before cursor
{C.GREEN}Ctrl+U{C.RESET}        Delete to beginning of line
{C.GREEN}Ctrl+K{C.RESET}        Delete to end of line

{C.YELLOW}These are standard in most Unix terminals!{C.RESET}""")
    pause()

    progress.complete_lesson("keys_advanced")
    progress.complete_lesson("keys_6")
    progress.complete_lesson("keys_7")
    progress.complete_lesson("keys_8")
    progress.complete_lesson("keys_9")
    progress.complete_lesson("keys_10")
    progress.check_module_achievements()


def _lesson_special(progress):
    hr_fancy("🎓 Special Input Tricks", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Two killer features hidden in plain sight.", color=C.WHITE)
    pause()

    info_box("1️⃣  @ File Mentions — Context Injection", f"""Type @ followed by a filename to add it to the AI's context.

{C.GREEN}Examples:{C.RESET}
  @src/app.ts            — adds a specific file
  @package.json          — adds package.json
  @tests/               — adds a directory listing

{C.YELLOW}Why it matters:{C.RESET}
  The AI can only help with what it can see. File mentions
  are the fastest way to give it the right context.

{C.CYAN}Power move:{C.RESET}
  "Fix the bug in @src/auth.ts based on @tests/auth.test.ts"
  → AI sees both files and understands the relationship.""")
    pause()

    info_box("2️⃣  ! Shell Bypass — Direct Commands", f"""Prefix any command with ! to run it in your shell directly.

{C.GREEN}Examples:{C.RESET}
  !ls -la               — list files
  !git status           — check git status
  !npm test             — run tests
  !docker ps            — check containers

{C.YELLOW}Why use it:{C.RESET}
  • Faster than asking the AI to run a command
  • No AI processing overhead
  • Output stays in your terminal
  • The AI can reference the output in later prompts

{C.RED}Not the same as:{C.RESET} asking AI to run a command
  (which goes through the tool system with confirmations)""")
    pause()

    progress.complete_lesson("keys_special")
    progress.complete_lesson("keys_11")
    progress.complete_lesson("keys_12")
    progress.complete_lesson("keyboard_shortcuts")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "What does Shift+Tab do in the Copilot CLI?",
            ["Undo last action", "Cycle through modes (Interactive/Plan/Autopilot)",
             "Tab completion", "Insert spaces"],
            1,
            "Shift+Tab cycles: Interactive → Plan → Autopilot → Interactive",
            "beginner", "Think about switching between different AI behaviors."
        ),
        Question(
            "How do you add a file to the AI's context?",
            ["Drag and drop", "Type @ followed by the filename",
             "/add-file <name>", "Copy-paste the contents"],
            1,
            "@ mentions are the fastest way to give the AI context about files.",
            "beginner", "It uses a social-media-like syntax."
        ),
        Question(
            "What does the ! prefix do?",
            ["Runs a shell command directly", "Negates the previous command",
             "Enters admin mode", "Shows command history"],
            0,
            "!command bypasses the AI and runs directly in your shell.",
            "beginner", "Think of it as a 'shell escape'."
        ),
        Question(
            "What does Ctrl+S do (vs. Enter)?",
            ["Saves the file", "Runs the prompt but keeps the text in input",
             "Takes a screenshot", "Submits silently"],
            1,
            "Ctrl+S preserves your input for iteration — great for refining prompts.",
            "intermediate", "Think about iterating on something."
        ),
        Question(
            "What does Ctrl+T toggle?",
            ["Terminal theme", "Reasoning/thinking display",
             "Tab width", "Timestamps"],
            1,
            "Ctrl+T shows or hides the AI's chain-of-thought reasoning.",
            "intermediate", "It lets you see inside the AI's 'thinking'."
        ),
        Question(
            "How do you open your input in $EDITOR?",
            ["Ctrl+E", "Ctrl+X → Ctrl+E", "Ctrl+O", "Alt+E"],
            1,
            "Two-step shortcut: Ctrl+X first, then Ctrl+E. Opens in your $EDITOR.",
            "advanced", "It's a two-key sequence, not a single shortcut."
        ),
        Question(
            "What happens when you triple-press Ctrl+C?",
            ["Force quits the CLI", "Clears the screen",
             "Exits the CLI entirely", "Restarts the session"],
            2,
            "Single=cancel operation, double=clear line, triple=exit CLI.",
            "intermediate", "Each press escalates the action."
        ),
        Question(
            "What does Ctrl+W delete?",
            ["Whole line", "Word before cursor",
             "Window content", "Whitespace"],
            1,
            "Ctrl+W deletes the word before the cursor (standard readline).",
            "intermediate", "W is for Word."
        ),
        FillInQuestion(
            "What key do you press to cancel the current AI operation?",
            ["esc", "escape"],
            "Esc cancels the current operation without clearing your input.",
            "beginner", "It's the universal 'cancel' key."
        ),
        ScenarioQuestion(
            "You're debugging a function. You need the AI to see the source file, "
            "the test file, and the latest git diff. You want to do this in a single prompt.",
            "How do you construct this prompt?",
            [
                "Copy-paste all three files into the prompt",
                "@src/utils.ts @tests/utils.test.ts then ask about git diff",
                "/add-file src/utils.ts && /add-file tests/utils.test.ts",
                "Use /context to load everything"
            ],
            1,
            "@ mentions let you reference multiple files inline. The AI can run !git diff itself.",
            "advanced"
        ),
    ]
    run_quiz(questions, progress, "keyboard_shortcuts", "Keyboard Shortcuts Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "shortcuts_efficiency",
        "title": "Speed Coding Session",
        "description": "You're in a fast-paced coding session. Use the right\n"
                       "shortcuts to maximize your efficiency.",
        "difficulty": "intermediate",
        "steps": [
            {
                "prompt": "You want to quickly check git status without AI processing. What do you type?",
                "options": ["git status", "'check my git status'", "!git status", "/git status"],
                "correct": 2,
                "success_msg": "✓ The ! prefix runs shell commands directly — instant results!",
                "fail_msg": "!git status runs directly in the shell, no AI overhead.",
                "explanation": "Shell bypass (!) is perfect for quick status checks."
            },
            {
                "prompt": "Your prompt needs work. You want to refine it by trying variations. How do you submit it?",
                "options": ["Press Enter", "Press Ctrl+S", "Press Ctrl+Enter", "Press Tab"],
                "correct": 1,
                "success_msg": "✓ Ctrl+S runs the prompt but keeps the text for editing!",
                "fail_msg": "Ctrl+S preserves your input — perfect for iteration.",
                "explanation": "Enter clears input; Ctrl+S preserves it for modification."
            },
            {
                "prompt": "The AI gave an unexpected answer. You want to see its reasoning. What shortcut?",
                "options": ["Ctrl+R", "Ctrl+T", "Ctrl+O", "Ctrl+D"],
                "correct": 1,
                "success_msg": "✓ Ctrl+T toggles the reasoning display!",
                "fail_msg": "Ctrl+T shows/hides the AI's thinking process.",
                "explanation": "Seeing the AI's reasoning helps you understand and refine your prompts."
            },
            {
                "prompt": "You need to write a complex multi-line prompt. What's the best approach?",
                "options": [
                    "Type it all on one line",
                    "Use multiple messages",
                    "Press Ctrl+X → Ctrl+E to edit in $EDITOR",
                    "Write it in a file first"
                ],
                "correct": 2,
                "success_msg": "✓ Ctrl+X → Ctrl+E opens your full text editor for complex prompts!",
                "fail_msg": "For complex prompts, open $EDITOR with Ctrl+X → Ctrl+E.",
                "explanation": "Your text editor gives you multi-line editing, syntax highlighting, and more."
            },
            {
                "prompt": "You want to switch to Plan mode for a risky refactoring. Fastest way?",
                "options": ["/plan", "Shift+Tab", "Ctrl+P", "Ctrl+M"],
                "correct": 1,
                "success_msg": "✓ Shift+Tab is the fastest way to cycle modes!",
                "fail_msg": "Shift+Tab cycles modes without typing a command.",
                "explanation": "/plan works too, but Shift+Tab is the keyboard-native way."
            },
        ]
    }
    run_scenario(scenario, progress)
