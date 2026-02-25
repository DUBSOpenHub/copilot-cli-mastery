"""Progress tracking, XP, levels, and achievements."""

import json
import os
from pathlib import Path

SAVE_FILE = os.path.expanduser("~/.copilot-mastery-progress.json")

LEVEL_THRESHOLDS = [
    (0, "Newcomer", "Just getting started"),
    (100, "Apprentice", "Learning the basics"),
    (300, "Navigator", "Finding your way around"),
    (600, "Practitioner", "Developing real skills"),
    (1000, "Specialist", "Deep knowledge forming"),
    (1500, "Expert", "Mastering advanced features"),
    (2200, "Virtuoso", "Orchestrating complex workflows"),
    (3000, "Architect", "Designing powerful solutions"),
    (4000, "Grandmaster", "Peak mastery achieved"),
    (5000, "CLI Wizard", "You ARE the CLI"),
]

ACHIEVEMENTS = {
    "first_lesson": ("First Steps", "Complete your first lesson", 10),
    "slash_beginner": ("Command Curious", "Learn 5 slash commands", 25),
    "slash_master": ("Slash Surgeon", "Master all slash commands", 100),
    "shortcut_student": ("Key Listener", "Learn 5 keyboard shortcuts", 25),
    "shortcut_master": ("Keyboard Ninja", "Master all keyboard shortcuts", 100),
    "mode_explorer": ("Mode Shifter", "Learn about all three modes", 50),
    "agent_aware": ("Agent Handler", "Complete the agents module", 75),
    "skill_builder": ("Skill Crafter", "Complete the skills module", 75),
    "mcp_integrator": ("Protocol Master", "Complete the MCP module", 75),
    "advanced_user": ("Power User", "Complete advanced techniques", 100),
    "config_guru": ("Config Guru", "Complete configuration module", 75),
    "quiz_perfect": ("Flawless", "Get a perfect score on any quiz", 50),
    "quiz_streak_3": ("Hat Trick", "Get 3 quizzes right in a row", 30),
    "quiz_streak_5": ("On Fire", "Get 5 quizzes right in a row", 50),
    "quiz_streak_10": ("Unstoppable", "Get 10 quizzes right in a row", 100),
    "all_modules": ("Completionist", "Complete every training module", 200),
    "scenario_solver": ("Problem Solver", "Complete your first scenario", 40),
    "scenario_master": ("Scenario Ace", "Complete all scenarios", 150),
    "speed_demon": ("Speed Demon", "Complete a quiz in under 30 seconds", 50),
    "explorer": ("Explorer", "Visit every section of the training tool", 30),
    "graduated": ("CLI Wizard Graduate", "Reach max level", 500),
}


class Progress:
    def __init__(self):
        self.xp = 0
        self.level = 0
        self.completed_lessons = set()
        self.completed_quizzes = set()
        self.completed_scenarios = set()
        self.achievements = set()
        self.quiz_streak = 0
        self.best_streak = 0
        self.total_questions_answered = 0
        self.total_correct = 0
        self.sections_visited = set()
        self.load()

    def load(self):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE) as f:
                    data = json.load(f)
                self.xp = data.get("xp", 0)
                self.level = data.get("level", 0)
                self.completed_lessons = set(data.get("completed_lessons", []))
                self.completed_quizzes = set(data.get("completed_quizzes", []))
                self.completed_scenarios = set(data.get("completed_scenarios", []))
                self.achievements = set(data.get("achievements", []))
                self.quiz_streak = data.get("quiz_streak", 0)
                self.best_streak = data.get("best_streak", 0)
                self.total_questions_answered = data.get("total_questions_answered", 0)
                self.total_correct = data.get("total_correct", 0)
                self.sections_visited = set(data.get("sections_visited", []))
            except (json.JSONDecodeError, IOError):
                pass

    def save(self):
        data = {
            "xp": self.xp,
            "level": self.level,
            "completed_lessons": list(self.completed_lessons),
            "completed_quizzes": list(self.completed_quizzes),
            "completed_scenarios": list(self.completed_scenarios),
            "achievements": list(self.achievements),
            "quiz_streak": self.quiz_streak,
            "best_streak": self.best_streak,
            "total_questions_answered": self.total_questions_answered,
            "total_correct": self.total_correct,
            "sections_visited": list(self.sections_visited),
        }
        try:
            with open(SAVE_FILE, "w") as f:
                json.dump(data, f, indent=2)
        except IOError:
            pass

    def add_xp(self, amount, reason=""):
        from engine.ui import print_xp, print_level_up
        old_level = self.level
        self.xp += amount
        print_xp(amount, reason)
        new_level = self._calc_level()
        if new_level > old_level:
            self.level = new_level
            _, title, _ = LEVEL_THRESHOLDS[min(new_level, len(LEVEL_THRESHOLDS) - 1)]
            print_level_up(old_level, new_level, title)
            if new_level >= len(LEVEL_THRESHOLDS) - 1:
                self.unlock("graduated")
        self.save()

    def _calc_level(self):
        for i in range(len(LEVEL_THRESHOLDS) - 1, -1, -1):
            if self.xp >= LEVEL_THRESHOLDS[i][0]:
                return i
        return 0

    def complete_lesson(self, lesson_id):
        if lesson_id not in self.completed_lessons:
            self.completed_lessons.add(lesson_id)
            self.add_xp(20, f"Completed lesson: {lesson_id}")
            if len(self.completed_lessons) == 1:
                self.unlock("first_lesson")
            self.save()

    def complete_quiz(self, quiz_id, score, total, elapsed=None):
        from engine.ui import print_success
        self.completed_quizzes.add(quiz_id)
        self.total_questions_answered += total
        self.total_correct += score
        xp = score * 15
        self.add_xp(xp, f"Quiz: {score}/{total} correct")
        if score == total:
            self.unlock("quiz_perfect")
        if elapsed and elapsed < 30 and score == total:
            self.unlock("speed_demon")
        self.save()

    def record_correct(self):
        self.quiz_streak += 1
        self.best_streak = max(self.best_streak, self.quiz_streak)
        if self.quiz_streak >= 3:
            self.unlock("quiz_streak_3")
        if self.quiz_streak >= 5:
            self.unlock("quiz_streak_5")
        if self.quiz_streak >= 10:
            self.unlock("quiz_streak_10")

    def record_incorrect(self):
        self.quiz_streak = 0

    def complete_scenario(self, scenario_id):
        if scenario_id not in self.completed_scenarios:
            self.completed_scenarios.add(scenario_id)
            self.add_xp(30, f"Scenario completed: {scenario_id}")
            if len(self.completed_scenarios) == 1:
                self.unlock("scenario_solver")
            self.save()

    def visit_section(self, section_id):
        self.sections_visited.add(section_id)
        all_sections = {
            "slash_commands", "keyboard_shortcuts", "modes", "agents",
            "skills", "mcp", "advanced", "configuration",
        }
        if all_sections.issubset(self.sections_visited):
            self.unlock("explorer")
        self.save()

    def unlock(self, achievement_id):
        from engine.ui import print_achievement
        if achievement_id in self.achievements:
            return
        if achievement_id not in ACHIEVEMENTS:
            return
        name, desc, bonus_xp = ACHIEVEMENTS[achievement_id]
        self.achievements.add(achievement_id)
        print_achievement(name, desc)
        self.xp += bonus_xp
        self.save()

    def get_level_info(self):
        idx = min(self.level, len(LEVEL_THRESHOLDS) - 1)
        _, title, desc = LEVEL_THRESHOLDS[idx]
        if idx < len(LEVEL_THRESHOLDS) - 1:
            next_threshold = LEVEL_THRESHOLDS[idx + 1][0]
        else:
            next_threshold = self.xp
        return {
            "level": self.level,
            "title": title,
            "desc": desc,
            "xp": self.xp,
            "next_xp": next_threshold,
            "xp_in_level": self.xp - LEVEL_THRESHOLDS[idx][0],
            "xp_needed": next_threshold - LEVEL_THRESHOLDS[idx][0],
        }

    def get_stats(self):
        accuracy = (
            int(100 * self.total_correct / self.total_questions_answered)
            if self.total_questions_answered > 0
            else 0
        )
        return {
            "lessons": len(self.completed_lessons),
            "quizzes": len(self.completed_quizzes),
            "scenarios": len(self.completed_scenarios),
            "achievements": len(self.achievements),
            "total_achievements": len(ACHIEVEMENTS),
            "accuracy": accuracy,
            "best_streak": self.best_streak,
            "total_answered": self.total_questions_answered,
        }

    def reset(self):
        self.xp = 0
        self.level = 0
        self.completed_lessons = set()
        self.completed_quizzes = set()
        self.completed_scenarios = set()
        self.achievements = set()
        self.quiz_streak = 0
        self.best_streak = 0
        self.total_questions_answered = 0
        self.total_correct = 0
        self.sections_visited = set()
        self.save()

    def check_module_achievements(self):
        """Check and award module-completion achievements."""
        module_checks = {
            "slash_beginner": lambda: len([l for l in self.completed_lessons if l.startswith("slash_")]) >= 5,
            "shortcut_student": lambda: len([l for l in self.completed_lessons if l.startswith("keys_")]) >= 5,
            "mode_explorer": lambda: "modes" in self.completed_lessons,
            "agent_aware": lambda: "agents" in self.completed_lessons,
            "skill_builder": lambda: "skills" in self.completed_lessons,
            "mcp_integrator": lambda: "mcp" in self.completed_lessons,
            "advanced_user": lambda: "advanced" in self.completed_lessons,
            "config_guru": lambda: "config" in self.completed_lessons,
        }
        for ach_id, check in module_checks.items():
            if ach_id not in self.achievements and check():
                self.unlock(ach_id)

        # Module-specific mastery achievements
        if "slash_commands" in self.completed_lessons:
            self.unlock("slash_master")
        if "keyboard_shortcuts" in self.completed_lessons:
            self.unlock("shortcut_master")

        # Scenario master: check all 8 module scenarios completed
        all_scenarios = {
            "slash_workflow", "shortcuts_efficiency", "mode_selection",
            "agent_orchestration", "skill_workflow", "mcp_setup",
            "expert_workflow", "config_setup",
        }
        if all_scenarios.issubset(self.completed_scenarios):
            self.unlock("scenario_master")

        # Check all modules complete
        all_mods = {"slash_commands", "keyboard_shortcuts", "modes", "agents", "skills", "mcp", "advanced", "config"}
        if all_mods.issubset(self.completed_lessons):
            self.unlock("all_modules")
