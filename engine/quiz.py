"""Interactive quiz engine with multiple question types."""

import time
import random
from engine.ui import (
    C, print_success, print_error, print_tip, hr, pause,
    box, print_difficulty, hr_fancy
)


class Question:
    def __init__(self, text, choices, correct, explanation="", difficulty="beginner", hint=""):
        self.text = text
        self.choices = choices
        self.correct = correct  # 0-indexed
        self.explanation = explanation
        self.difficulty = difficulty
        self.hint = hint


class FillInQuestion:
    def __init__(self, text, answers, explanation="", difficulty="beginner", hint=""):
        self.text = text
        self.answers = [a.lower().strip() for a in answers]  # list of acceptable answers
        self.explanation = explanation
        self.difficulty = difficulty
        self.hint = hint


class ScenarioQuestion:
    def __init__(self, scenario, question, choices, correct, explanation="", difficulty="intermediate"):
        self.scenario = scenario
        self.question = question
        self.choices = choices
        self.correct = correct
        self.explanation = explanation
        self.difficulty = difficulty


def run_quiz(questions, progress, quiz_id="general", title="Quiz"):
    """Run an interactive quiz and return (score, total)."""
    hr_fancy(f"🎯 {title}", C.BRIGHT_CYAN)
    print(f"\n  {C.WHITE}Answer the following questions to test your knowledge.{C.RESET}")
    print(f"  {C.DIM}Type the number of your answer, or 'h' for a hint, 'q' to quit.{C.RESET}\n")

    score = 0
    total = len(questions)
    start_time = time.time()
    streak = 0

    shuffled = list(questions)
    random.shuffle(shuffled)

    for i, q in enumerate(shuffled, 1):
        hr(color=C.BRIGHT_BLACK)
        print(f"\n  {C.BOLD}Question {i}/{total}{C.RESET}", end="")
        if hasattr(q, 'difficulty'):
            print(f"  {C.DIM}({q.difficulty}){C.RESET}", end="")
        if streak >= 3:
            print(f"  {C.BRIGHT_YELLOW}🔥 Streak: {streak}{C.RESET}", end="")
        print()

        if isinstance(q, ScenarioQuestion):
            print(f"\n  {C.BRIGHT_CYAN}📋 Scenario:{C.RESET}")
            for line in q.scenario.split("\n"):
                print(f"    {C.WHITE}{line}{C.RESET}")
            print(f"\n  {C.BOLD}{q.question}{C.RESET}\n")
        elif isinstance(q, FillInQuestion):
            print(f"\n  {C.BOLD}{q.text}{C.RESET}\n")
            got_answer = _ask_fill_in(q)
            if got_answer:
                score += 1
                streak += 1
                progress.record_correct()
                print_success("Correct!")
            else:
                streak = 0
                progress.record_incorrect()
                print_error(f"The answer was: {C.BOLD}{q.answers[0]}{C.RESET}")
            if q.explanation:
                print(f"    {C.DIM}💬 {q.explanation}{C.RESET}")
            continue
        else:
            print(f"\n  {C.BOLD}{q.text}{C.RESET}\n")

        for j, choice in enumerate(q.choices):
            print(f"    {C.CYAN}{j + 1}.{C.RESET} {choice}")
        print()

        hint_used = False
        while True:
            try:
                ans = input(f"  {C.BRIGHT_WHITE}Your answer ▸ {C.RESET}").strip().lower()
            except EOFError:
                ans = "q"

            if ans == "q":
                elapsed = time.time() - start_time
                progress.complete_quiz(quiz_id, score, i - 1, elapsed)
                return score, i - 1
            if ans == "h" and hasattr(q, 'hint') and q.hint:
                print_tip(q.hint)
                hint_used = True
                continue
            try:
                idx = int(ans) - 1
                if 0 <= idx < len(q.choices):
                    break
            except ValueError:
                pass
            print(f"  {C.DIM}Enter 1-{len(q.choices)}, 'h' for hint, or 'q' to quit{C.RESET}")

        if idx == q.correct:
            score += 1
            streak += 1
            progress.record_correct()
            points = 15 if not hint_used else 8
            print_success(f"Correct! (+{points} XP)")
        else:
            streak = 0
            progress.record_incorrect()
            print_error(f"Wrong! The answer was: {C.BOLD}{q.choices[q.correct]}{C.RESET}")

        if q.explanation:
            print(f"    {C.DIM}💬 {q.explanation}{C.RESET}")

    elapsed = time.time() - start_time

    # Results summary
    print()
    hr_fancy("📊 Results", C.BRIGHT_CYAN)
    pct = int(100 * score / total) if total > 0 else 0
    if pct == 100:
        grade_color = C.BRIGHT_GREEN
        grade = "PERFECT! 🌟"
    elif pct >= 80:
        grade_color = C.GREEN
        grade = "Excellent! 🎉"
    elif pct >= 60:
        grade_color = C.YELLOW
        grade = "Good job! 👍"
    elif pct >= 40:
        grade_color = C.BRIGHT_YELLOW
        grade = "Keep practicing! 📚"
    else:
        grade_color = C.RED
        grade = "Review the material! 📖"

    print(f"\n  {C.BOLD}Score:{C.RESET} {grade_color}{score}/{total} ({pct}%){C.RESET}")
    print(f"  {C.BOLD}Grade:{C.RESET} {grade_color}{grade}{C.RESET}")
    print(f"  {C.BOLD}Time:{C.RESET}  {C.WHITE}{int(elapsed)}s{C.RESET}")
    print()

    progress.complete_quiz(quiz_id, score, total, elapsed)
    pause()
    return score, total


def _ask_fill_in(q):
    """Ask a fill-in-the-blank question."""
    hint_used = False
    while True:
        try:
            ans = input(f"  {C.BRIGHT_WHITE}Type your answer ▸ {C.RESET}").strip().lower()
        except EOFError:
            return False

        if ans == "h" and q.hint:
            print_tip(q.hint)
            hint_used = True
            continue
        if ans == "q":
            return False

        return ans in q.answers


def run_scenario(scenario_data, progress):
    """Run an interactive scenario challenge."""
    from engine.ui import print_scenario

    sid = scenario_data["id"]
    print_scenario(scenario_data["title"], scenario_data["description"])
    print_difficulty(scenario_data.get("difficulty", "intermediate"))
    print()

    steps = scenario_data["steps"]
    completed = 0

    for i, step in enumerate(steps, 1):
        print(f"\n  {C.BRIGHT_CYAN}Step {i}/{len(steps)}:{C.RESET} {C.BOLD}{step['prompt']}{C.RESET}\n")

        for j, opt in enumerate(step["options"], 1):
            print(f"    {C.CYAN}{j}.{C.RESET} {opt}")
        print()

        while True:
            try:
                ans = input(f"  {C.BRIGHT_WHITE}Your choice ▸ {C.RESET}").strip()
            except EOFError:
                return
            try:
                idx = int(ans) - 1
                if 0 <= idx < len(step["options"]):
                    break
            except ValueError:
                pass
            print(f"  {C.DIM}Enter 1-{len(step['options'])}{C.RESET}")

        if idx == step["correct"]:
            completed += 1
            print_success(step.get("success_msg", "Correct approach!"))
        else:
            print_error(step.get("fail_msg", "Not the best approach."))
            print(f"    {C.DIM}Better: {step['options'][step['correct']]}{C.RESET}")

        if step.get("explanation"):
            print(f"\n    {C.DIM}💬 {step['explanation']}{C.RESET}")

    print()
    hr_fancy("Scenario Complete", C.BRIGHT_GREEN)
    pct = int(100 * completed / len(steps))
    print(f"\n  {C.BOLD}Steps correct:{C.RESET} {completed}/{len(steps)} ({pct}%)")

    if pct >= 70:
        progress.complete_scenario(sid)
        print_success("Scenario passed!")
    else:
        print(f"\n  {C.YELLOW}Try again to pass this scenario (need 70%+){C.RESET}")

    pause()
