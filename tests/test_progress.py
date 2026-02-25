"""Tests for the progress tracking engine."""

import json
import os

import pytest
from engine.progress import Progress, ACHIEVEMENTS, LEVEL_THRESHOLDS, SAVE_FILE
import engine.progress as pm


def test_fresh_state(progress):
    assert progress.xp == 0
    assert progress.level == 0
    assert len(progress.completed_lessons) == 0
    assert len(progress.achievements) == 0


def test_save_load_round_trip(progress):
    progress.xp = 500
    progress.level = 3
    progress.completed_lessons.add("test_lesson")
    progress.achievements.add("first_lesson")
    progress.quiz_streak = 4
    progress.best_streak = 7
    progress.total_questions_answered = 20
    progress.total_correct = 15
    progress.sections_visited.add("agents")
    progress.save()

    p2 = Progress()
    assert p2.xp == 500
    assert p2.level == 3
    assert "test_lesson" in p2.completed_lessons
    assert "first_lesson" in p2.achievements
    assert p2.quiz_streak == 4
    assert p2.best_streak == 7
    assert p2.total_questions_answered == 20
    assert p2.total_correct == 15
    assert "agents" in p2.sections_visited


def test_level_calculation(progress):
    thresholds = [
        (0, 0), (100, 1), (300, 2), (600, 3), (1000, 4),
        (1500, 5), (2200, 6), (3000, 7), (4000, 8), (5000, 9), (99999, 9),
    ]
    for xp, expected in thresholds:
        progress.xp = xp
        assert progress._calc_level() == expected, f"XP={xp}"


def test_level_info(progress):
    progress.xp = 150
    progress.level = 1
    info = progress.get_level_info()
    assert info["level"] == 1
    assert info["title"] == "Apprentice"
    assert info["xp_in_level"] == 50
    assert info["xp_needed"] == 200


def test_stats_accuracy(progress):
    progress.total_questions_answered = 10
    progress.total_correct = 7
    assert progress.get_stats()["accuracy"] == 70


def test_stats_zero_division(progress):
    assert progress.get_stats()["accuracy"] == 0


def test_streak_tracking(progress):
    for _ in range(5):
        progress.record_correct()
    assert progress.quiz_streak == 5
    assert progress.best_streak == 5
    progress.record_incorrect()
    assert progress.quiz_streak == 0
    assert progress.best_streak == 5


def test_reset(progress):
    progress.xp = 999
    progress.completed_lessons.add("x")
    progress.achievements.add("y")
    progress.reset()
    assert progress.xp == 0
    assert len(progress.completed_lessons) == 0
    assert len(progress.achievements) == 0


def test_corrupt_save_file():
    with open(pm.SAVE_FILE, "w") as f:
        f.write("NOT VALID JSON {{{")
    p = Progress()
    assert p.xp == 0


def test_max_level(progress):
    progress.xp = 999999
    progress.level = 9
    info = progress.get_level_info()
    assert info["title"] == "CLI Wizard"
    assert info["xp_needed"] >= 0


def test_duplicate_lesson_idempotent(progress):
    progress.complete_lesson("dup_test")
    xp1 = progress.xp
    progress.complete_lesson("dup_test")
    assert progress.xp == xp1


def test_duplicate_scenario_idempotent(progress):
    progress.complete_scenario("sc_dup")
    xp1 = progress.xp
    progress.complete_scenario("sc_dup")
    assert progress.xp == xp1


def test_unlock_invalid_achievement(progress):
    progress.unlock("nonexistent")
    assert "nonexistent" not in progress.achievements


def test_visit_all_sections(progress):
    sections = [
        "slash_commands", "keyboard_shortcuts", "modes", "agents",
        "skills", "mcp", "advanced", "configuration",
    ]
    for s in sections:
        progress.visit_section(s)
    assert len(progress.sections_visited) == 8
    progress.save()
    p2 = Progress()
    assert len(p2.sections_visited) == 8


def test_module_achievements(progress):
    for ml in ["slash_commands", "keyboard_shortcuts", "modes", "agents",
               "skills", "mcp", "advanced", "config"]:
        progress.completed_lessons.add(ml)
    for i in range(1, 6):
        progress.completed_lessons.add(f"slash_{i}")
        progress.completed_lessons.add(f"keys_{i}")
    progress.check_module_achievements()
    assert "mode_explorer" in progress.achievements
    assert "all_modules" in progress.achievements


def test_achievement_data_integrity():
    assert len(ACHIEVEMENTS) == 21
    for ach_id, (name, desc, xp) in ACHIEVEMENTS.items():
        assert xp > 0
        assert name
        assert desc


def test_level_thresholds_monotonic():
    for i in range(1, len(LEVEL_THRESHOLDS)):
        assert LEVEL_THRESHOLDS[i][0] > LEVEL_THRESHOLDS[i - 1][0]
