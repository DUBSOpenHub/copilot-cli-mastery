#!/usr/bin/env python3
"""
Copilot CLI Mastery — The Interactive Training System
=====================================================
From Zero to CLI Wizard. Master every feature of the GitHub Copilot CLI
through interactive lessons, quizzes, scenarios, and challenges.

Run: python3 mastery.py
"""

import sys
import os
import argparse
import textwrap

# Ensure we can import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.ui import (
    C, clear, show_splash, hr_fancy, hr, menu, pause, box, info_box,
    print_centered, progress_bar, print_tip, print_success, type_text,
    print_shortcut, print_command, print_difficulty
)
from engine.progress import Progress, ACHIEVEMENTS, LEVEL_THRESHOLDS

from modules import slash_commands, keyboard_shortcuts, modes, agents, skills, mcp, advanced, configuration

# ── Module Registry ──────────────────────────────────────────────
# Adding a module? Just append an entry here — no other file edits needed.
MODULE_REGISTRY = [
    {"key": "slash",    "icon": "📖", "color": C.GREEN,   "label": "Slash Commands",       "desc": "all 35+ commands",              "lesson_id": "slash_commands",    "mod": slash_commands},
    {"key": "keys",     "icon": "⌨️",  "color": C.YELLOW,  "label": "Keyboard Shortcuts",   "desc": "20+ shortcuts",                 "lesson_id": "keyboard_shortcuts","mod": keyboard_shortcuts},
    {"key": "modes",    "icon": "🔄", "color": C.BLUE,    "label": "Interaction Modes",     "desc": "Interactive, Plan, Autopilot",  "lesson_id": "modes",             "mod": modes},
    {"key": "agents",   "icon": "🤖", "color": C.MAGENTA, "label": "Agent System",          "desc": "built-in & custom agents",      "lesson_id": "agents",            "mod": agents},
    {"key": "skills",   "icon": "🎨", "color": C.CYAN,    "label": "Skills System",         "desc": "AI capabilities",               "lesson_id": "skills",            "mod": skills},
    {"key": "mcp",      "icon": "🔌", "color": C.GREEN,   "label": "MCP Integration",       "desc": "external tools & servers",      "lesson_id": "mcp",               "mod": mcp},
    {"key": "advanced", "icon": "🚀", "color": C.RED,     "label": "Advanced Techniques",   "desc": "expert workflows",              "lesson_id": "advanced",          "mod": advanced},
    {"key": "config",   "icon": "⚙️",  "color": C.YELLOW,  "label": "Configuration",         "desc": "config, permissions, LSP",      "lesson_id": "config",            "mod": configuration},
]


def show_dashboard(progress):
    """Show the user's progress dashboard."""
    info = progress.get_level_info()
    stats = progress.get_stats()

    hr_fancy(f"📊 Your Dashboard — Level {info['level']}: {info['title']}", C.BRIGHT_CYAN)
    print()

    # XP bar
    progress_bar(
        info['xp_in_level'], info['xp_needed'],
        width=35, label=f"  {C.BRIGHT_MAGENTA}⭐ XP{C.RESET}",
        color=C.BRIGHT_MAGENTA
    )
    print(f"    {C.DIM}Total: {info['xp']} XP | Next level: {info['next_xp']} XP{C.RESET}")
    print()

    # Stats
    print(f"  {C.BOLD}📚 Lessons completed:{C.RESET}     {C.GREEN}{stats['lessons']}{C.RESET}")
    print(f"  {C.BOLD}🎯 Quizzes completed:{C.RESET}     {C.GREEN}{stats['quizzes']}{C.RESET}")
    print(f"  {C.BOLD}🧩 Scenarios completed:{C.RESET}   {C.GREEN}{stats['scenarios']}{C.RESET}")
    print(f"  {C.BOLD}📊 Quiz accuracy:{C.RESET}         {C.GREEN}{stats['accuracy']}%{C.RESET} ({stats['total_answered']} questions)")
    print(f"  {C.BOLD}🔥 Best streak:{C.RESET}           {C.GREEN}{stats['best_streak']}{C.RESET}")
    print(f"  {C.BOLD}🏆 Achievements:{C.RESET}          {C.GREEN}{stats['achievements']}/{stats['total_achievements']}{C.RESET}")
    print()

    # Module completion
    hr(color=C.BRIGHT_BLACK)
    print(f"\n  {C.BOLD}Module Progress:{C.RESET}")
    for m in MODULE_REGISTRY:
        done = m["lesson_id"] in progress.completed_lessons
        icon = f"{C.GREEN}✅{C.RESET}" if done else f"{C.BRIGHT_BLACK}⬜{C.RESET}"
        print(f"    {icon} {m['label']}")
    print()


def show_achievements(progress):
    """Show all achievements."""
    hr_fancy("🏆 Achievements", C.BRIGHT_YELLOW)
    print()

    unlocked = 0
    for ach_id, (name, desc, xp) in sorted(ACHIEVEMENTS.items()):
        if ach_id in progress.achievements:
            print(f"  {C.BRIGHT_YELLOW}🏆{C.RESET} {C.BOLD}{name}{C.RESET}")
            print(f"     {C.DIM}{desc} (+{xp} XP){C.RESET}")
            unlocked += 1
        else:
            print(f"  {C.BRIGHT_BLACK}🔒 {name}{C.RESET}")
            print(f"     {C.BRIGHT_BLACK}{desc} (+{xp} XP){C.RESET}")
    print()
    print(f"  {C.BOLD}Unlocked:{C.RESET} {unlocked}/{len(ACHIEVEMENTS)}")
    print()
    pause()


def show_quick_reference(progress):
    """Show the complete quick reference card."""
    while True:
        hr_fancy("📋 Quick Reference Card", C.BRIGHT_CYAN)
        print()

        result = menu([
            ("📝 All Slash Commands", "slash"),
            ("⌨️  All Keyboard Shortcuts", "keys"),
            ("🔄 Modes Overview", "modes"),
            ("🤖 Agent Quick Reference", "agents"),
            ("🔌 MCP Quick Reference", "mcp"),
            ("📄 Instruction Files Map", "instructions"),
            ("⚙️  Config Files Map", "config"),
        ], "Select reference")

        if result is None:
            return

        print()
        if result == "slash":
            from modules.slash_commands import COMMAND_CATEGORIES
            for cat, cmds in COMMAND_CATEGORIES.items():
                print(f"\n  {C.BOLD}{cat}{C.RESET}")
                for cmd, desc in cmds:
                    print_command(cmd, desc)
            print()
            pause()

        elif result == "keys":
            from modules.keyboard_shortcuts import SHORTCUTS
            for cat, shortcuts in SHORTCUTS.items():
                print(f"\n  {C.BOLD}{cat}{C.RESET}")
                for keys, desc in shortcuts:
                    print_shortcut(keys, desc)
            print()
            pause()

        elif result == "modes":
            print(f"  {C.GREEN}{C.BOLD}Interactive{C.RESET} (default) — AI acts immediately, confirms risky ops")
            print(f"  {C.YELLOW}{C.BOLD}Plan{C.RESET}        (/plan, Shift+Tab) — AI creates plan, you approve")
            print(f"  {C.MAGENTA}{C.BOLD}Autopilot{C.RESET}   (/experimental) — AI acts without confirmation")
            print()
            pause()

        elif result == "agents":
            print(f"  {C.CYAN}{C.BOLD}explore{C.RESET}          — Fast codebase Q&A (Haiku, read-only)")
            print(f"  {C.YELLOW}{C.BOLD}task{C.RESET}             — Run commands, tests, builds (Haiku)")
            print(f"  {C.GREEN}{C.BOLD}general-purpose{C.RESET}  — Full capability agent (Sonnet)")
            print(f"  {C.MAGENTA}{C.BOLD}code-review{C.RESET}      — Analyze changes, never modifies (all tools)")
            print(f"\n  {C.DIM}Custom: ~/.copilot/agents/ | .github/agents/ | org-level{C.RESET}")
            print()
            pause()

        elif result == "mcp":
            print(f"  {C.GREEN}Built-in:{C.RESET}  GitHub MCP server (search, PRs, issues)")
            print(f"  {C.YELLOW}Add:{C.RESET}       /mcp add <name> <command>")
            print(f"  {C.CYAN}Config:{C.RESET}    ~/.copilot/mcp-config.json")
            print(f"  {C.CYAN}Project:{C.RESET}   .github/mcp-config.json")
            print(f"  {C.WHITE}List:{C.RESET}      /mcp (no arguments)")
            print()
            pause()

        elif result == "instructions":
            print(f"  {C.GREEN}Global:{C.RESET}     ~/.copilot/copilot-instructions.md")
            print(f"  {C.YELLOW}Repo:{C.RESET}       .github/copilot-instructions.md")
            print(f"  {C.CYAN}Model:{C.RESET}      CLAUDE.md | GEMINI.md")
            print(f"  {C.MAGENTA}Agent:{C.RESET}      AGENTS.md")
            print(f"  {C.WHITE}Path:{C.RESET}       .github/instructions/*.instructions.md")
            print(f"\n  {C.DIM}Priority: Global → Repo → Model → Agent → Path{C.RESET}")
            print()
            pause()

        elif result == "config":
            print(f"  {C.GREEN}Main:{C.RESET}       ~/.copilot/config.json")
            print(f"  {C.YELLOW}MCP:{C.RESET}        ~/.copilot/mcp-config.json")
            print(f"  {C.CYAN}LSP:{C.RESET}        lsp-config.json | .github/lsp.json")
            print(f"  {C.MAGENTA}Agents:{C.RESET}     ~/.copilot/agents/*.md")
            print(f"  {C.WHITE}Project:{C.RESET}    .github/agents/*.md")
            print(f"  {C.WHITE}Project:{C.RESET}    .github/copilot-instructions.md")
            print()
            pause()


def export_reference():
    """Export a complete text cheatsheet to a file and return the path."""
    from modules.slash_commands import COMMAND_CATEGORIES
    from modules.keyboard_shortcuts import SHORTCUTS
    from pathlib import Path

    out = Path(__file__).resolve().parent / "copilot_cli_reference.txt"
    lines = ["Copilot CLI Mastery — Quick Reference Cheatsheet\n",
             "=" * 50 + "\n\n",
             "SLASH COMMANDS\n",
             "-" * 40 + "\n"]
    for cat, cmds in COMMAND_CATEGORIES.items():
        lines.append(f"\n{cat}\n")
        for cmd, desc in cmds:
            lines.append(f"  {cmd:<24} {desc}\n")
    lines.append("\n\nKEYBOARD SHORTCUTS\n")
    lines.append("-" * 40 + "\n")
    for cat, shortcuts in SHORTCUTS.items():
        lines.append(f"\n{cat}\n")
        for keys, desc in shortcuts:
            lines.append(f"  {keys:<22} {desc}\n")
    out.write_text("".join(lines))
    return out


def show_scenario_arena(progress):
    """Run real-world scenario challenges (ported from Codex runner-up)."""
    from data.validation import SCENARIOS

    while True:
        hr_fancy("🏟️  Scenario Arena — Real-World Challenges", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Type your command/shortcut workflow to solve each scenario.{C.RESET}\n")

        items = []
        for i, scenario in enumerate(SCENARIOS, 1):
            solved = scenario["title"] in progress.completed_scenarios
            icon = f"{C.GREEN}✅{C.RESET}" if solved else f"{C.BRIGHT_BLACK}⬜{C.RESET}"
            items.append((f"{icon} [{scenario['difficulty']}] {scenario['title']}", i))
        result = menu(items, "Select scenario")

        if result is None or result == "quit":
            return

        scenario = SCENARIOS[result - 1]
        print()
        hr_fancy(f"📋 {scenario['title']}", C.BRIGHT_CYAN)
        print_difficulty(scenario["difficulty"])
        print()
        for line in textwrap.wrap(scenario["prompt"], 70):
            print(f"    {C.WHITE}{line}{C.RESET}")
        print()

        try:
            answer = input(f"  {C.BRIGHT_WHITE}Your command/shortcut workflow ▸ {C.RESET}").strip()
        except (EOFError, KeyboardInterrupt):
            return

        lowered = answer.lower()
        matched = [t for t in scenario["required"] if t.lower() in lowered]
        if len(matched) == len(scenario["required"]):
            print_success("Mission cleared!")
            progress.complete_scenario(scenario["title"])
        else:
            from engine.ui import print_error
            print_error("Not enough key moves included.")
            print(f"    {C.DIM}Needed: {', '.join(scenario['required'])}{C.RESET}")
            print(f"    {C.DIM}Reference: {scenario['model_answer']}{C.RESET}")
        pause()


def show_final_exam(progress):
    """Run the comprehensive final exam."""
    from engine.quiz import Question, ScenarioQuestion, FillInQuestion, run_quiz

    hr_fancy("🎓 FINAL EXAM — CLI Mastery Certification", C.BRIGHT_YELLOW)
    print()
    print_difficulty("expert")
    print(f"\n  {C.WHITE}20 questions across ALL modules.{C.RESET}")
    print(f"  {C.WHITE}Score 80%+ to earn the {C.BRIGHT_YELLOW}CLI Wizard{C.RESET}{C.WHITE} achievement.{C.RESET}\n")

    if not menu([("Begin Final Exam", True)], "Ready?", back_option=True):
        return

    questions = [
        Question("What does /compact do?",
            ["Minifies code", "Summarizes conversation to free context", "Compresses files", "Minimizes output"],
            1, difficulty="intermediate"),
        Question("Which shortcut cycles through modes?",
            ["Ctrl+M", "Shift+Tab", "Ctrl+Tab", "Alt+M"], 1, difficulty="beginner"),
        Question("What are the four built-in agents?",
            ["explore, task, general-purpose, code-review", "search, build, test, deploy",
             "read, write, execute, review", "fast, standard, premium, expert"], 0, difficulty="intermediate"),
        FillInQuestion("Type the shell bypass prefix (one character):",
            ["!", "!"], difficulty="beginner"),
        Question("Where are personal custom agents stored?",
            [".github/agents/", "~/.copilot/agents/", "~/.agents/", "/etc/agents/"], 1, difficulty="intermediate"),
        Question("What does MCP stand for?",
            ["Machine Code Protocol", "Model Context Protocol", "Multi-Client Platform", "Managed Connection Port"],
            1, difficulty="beginner"),
        Question("Which flag skips all confirmation prompts?",
            ["--fast", "--allow-all / --yolo", "--unsafe", "--auto"], 1, difficulty="intermediate"),
        Question("What file holds project-level LSP config?",
            ["lsp.json", ".github/lsp.json", ".lsp/config.json", "tsconfig.json"], 1, difficulty="expert"),
        ScenarioQuestion(
            "You're at 90% context capacity mid-session. You finished the auth module and are starting payments.",
            "What do you do?",
            ["/clear", "/compact", "Start new session", "Keep going"], 1, difficulty="advanced"),
        Question("What does Ctrl+T toggle?",
            ["Theme", "AI reasoning/thinking display", "Timestamps", "Tab width"], 1, difficulty="intermediate"),
        Question("How do you resume the last session from CLI?",
            ["copilot --resume", "copilot --continue", "copilot --last", "copilot resume"], 1, difficulty="intermediate"),
        FillInQuestion("What syntax adds a file to AI context? (e.g., ??? filename.ts)",
            ["@", "@filename.ts"], difficulty="beginner"),
        Question("Which agent uses the Haiku model for speed?",
            ["general-purpose", "code-review", "explore", "custom"], 2, difficulty="intermediate"),
        Question("Where do team-shared instruction files go?",
            ["~/.copilot/", ".github/copilot-instructions.md", "CLAUDE.md", "~/.instructions/"], 1, difficulty="advanced"),
        ScenarioQuestion(
            "You need to review 50 changed files before merging a PR. You only want real issues flagged.",
            "What command?",
            ["/diff", "/review", "/agent code-review", "/check"], 1, difficulty="intermediate"),
        Question("What does /delegate do?",
            ["Delegates permissions", "Spawns a coding agent for a complex task",
             "Delegates to another user", "Forwards to IDE"], 1, difficulty="intermediate"),
        Question("What Ctrl combo opens input in $EDITOR?",
            ["Ctrl+E", "Ctrl+X → Ctrl+E", "Ctrl+O", "Alt+E"], 1, difficulty="advanced"),
        Question("What does /reset-allowed-tools do?",
            ["Resets tools", "Re-enables confirmation prompts", "Resets to defaults", "Clears cache"], 1, difficulty="intermediate"),
        ScenarioQuestion(
            "Your monorepo has Python backend and React frontend with different coding standards.",
            "Best configuration approach?",
            ["One big instruction file", ".github/instructions/*.instructions.md path-specific files",
             "Different branches", "Mention standards each time"], 1, difficulty="advanced"),
        Question("Triple-pressing Ctrl+C does what?",
            ["Force quit", "Clear all", "Exit the CLI", "Restart"], 2, difficulty="intermediate"),
    ]

    score, total = run_quiz(questions, progress, "final_exam", "Final Exam")
    if total > 0 and score / total >= 0.8:
        progress.unlock("graduated")
        print()
        box(f"{C.BRIGHT_YELLOW}🎓 CERTIFICATION EARNED: Copilot CLI Master{C.RESET}\n\n"
            f"You have demonstrated expert-level knowledge of\n"
            f"the GitHub Copilot CLI. You are now a CLI Wizard!",
            color=C.BRIGHT_YELLOW)
        print()


def main():
    progress = Progress()

    show_splash(progress)

    while True:
        info = progress.get_level_info()

        print(f"\n  {C.BRIGHT_MAGENTA}⭐{C.RESET} {C.BOLD}Level {info['level']}: {info['title']}{C.RESET}"
              f"  {C.DIM}({info['xp']} XP){C.RESET}")
        progress_bar(info['xp_in_level'], info['xp_needed'], width=25,
                     label=f"  ", color=C.BRIGHT_MAGENTA)

        # Build module menu items from registry
        module_items = []
        for m in MODULE_REGISTRY:
            label = f"{m['icon']} {m['color']}{m['label']}{C.RESET}".ljust(40) + f"— {m['desc']}"
            module_items.append((label, m["key"]))

        result = menu(module_items + [
            (f"🏟️  {C.BRIGHT_CYAN}Scenario Arena{C.RESET}        — real-world challenges", "scenarios"),
            ("", None),
            (f"📊 Dashboard & Progress", "dashboard"),
            (f"🏆 Achievements ({len(progress.achievements)}/{len(ACHIEVEMENTS)})", "achievements"),
            (f"📋 Quick Reference Card", "reference"),
            (f"📤 Export Reference Cheatsheet", "export"),
            (f"🎓 Final Exam — CLI Wizard Certification", "exam"),
            ("", None),
            (f"🔄 Reset Progress", "reset"),
        ], "Select module", back_option=False)

        if result is None:
            continue
        elif result == "quit":
            print(f"\n  {C.BRIGHT_CYAN}Thanks for training! Keep practicing! 🚀{C.RESET}\n")
            break

        # Dispatch to registered module
        dispatched = False
        for m in MODULE_REGISTRY:
            if result == m["key"]:
                m["mod"].run_lesson(progress)
                dispatched = True
                break

        if dispatched:
            continue
        elif result == "dashboard":
            show_dashboard(progress)
            pause()
        elif result == "achievements":
            show_achievements(progress)
        elif result == "scenarios":
            show_scenario_arena(progress)
        elif result == "reference":
            show_quick_reference(progress)
        elif result == "export":
            out_path = export_reference()
            progress.add_xp(20, "Exported reference cheatsheet")
            print_success(f"Reference exported to: {out_path}")
            pause()
        elif result == "exam":
            show_final_exam(progress)
        elif result == "reset":
            from engine.ui import confirm
            if confirm("Reset ALL progress? This cannot be undone."):
                progress.reset()
                print_success("Progress reset.")
                pause()


def show_splash(progress):
    """Show splash screen with animation."""
    from engine.ui import show_splash as _splash
    _splash()

    if progress.xp > 0:
        info = progress.get_level_info()
        print(f"  {C.BRIGHT_WHITE}Welcome back, {C.BOLD}{info['title']}{C.RESET}!")
        print(f"  {C.DIM}Level {info['level']} • {info['xp']} XP • "
              f"{len(progress.achievements)} achievements{C.RESET}")
    else:
        type_text("  Welcome to Copilot CLI Mastery Training!", color=C.BRIGHT_WHITE)
        type_text("  Master every feature of the GitHub Copilot CLI.", color=C.DIM)

    print()
    print(f"  {C.DIM}Type a number to select, 'q' to quit at any time.{C.RESET}")


def run_batch_validation():
    """Non-interactive validation: curriculum + all module imports + progress engine.

    Suitable for CI pipelines. Returns exit code 0 on success, 1 on failure.
    """
    from data.validation import validate_curriculum

    errors = []

    # 1. Curriculum coverage
    curr_errors = validate_curriculum()
    errors.extend(curr_errors)

    # 2. All modules importable with run_lesson
    for mod in [slash_commands, keyboard_shortcuts, modes, agents, skills, mcp, advanced, configuration]:
        if not hasattr(mod, 'run_lesson') or not callable(mod.run_lesson):
            errors.append(f"Module {mod.__name__} missing callable run_lesson()")

    # 3. Progress engine round-trip
    import tempfile, json
    import engine.progress as pm
    old_save = pm.SAVE_FILE
    pm.SAVE_FILE = tempfile.mktemp(suffix='.json')
    try:
        p = pm.Progress()
        p.xp = 42
        p.completed_lessons.add("_ci_test")
        p.save()
        p2 = pm.Progress()
        if p2.xp != 42 or "_ci_test" not in p2.completed_lessons:
            errors.append("Progress save/load round-trip failed")
    finally:
        if os.path.exists(pm.SAVE_FILE):
            os.remove(pm.SAVE_FILE)
        pm.SAVE_FILE = old_save

    # 4. Export reference
    ref_path = export_reference()
    if not os.path.exists(ref_path):
        errors.append(f"Reference export failed: {ref_path}")

    if errors:
        print("Batch validation FAILED:")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("Batch validation PASSED: curriculum, modules, progress, and export all OK.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Copilot CLI Mastery Training Tool")
    parser.add_argument("--self-test", action="store_true",
                        help="Validate curriculum coverage and exports, then exit")
    parser.add_argument("--non-interactive", action="store_true",
                        help="Run full batch validation (no user input), for CI pipelines")
    parser.add_argument("--no-color", action="store_true",
                        help="Disable ANSI color codes in output")
    args = parser.parse_args()

    if args.self_test:
        from data.validation import validate_curriculum
        errors = validate_curriculum()
        if errors:
            print("Self-test FAILED:")
            for err in errors:
                print(f"  - {err}")
            sys.exit(1)
        ref_path = export_reference()
        print(f"Self-test PASSED: curriculum coverage is complete.")
        print(f"Reference exported to: {ref_path}")
        sys.exit(0)

    if args.non_interactive:
        sys.exit(run_batch_validation())

    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n  {C.BRIGHT_CYAN}Training paused. Your progress is saved! 🚀{C.RESET}\n")
        sys.exit(0)
