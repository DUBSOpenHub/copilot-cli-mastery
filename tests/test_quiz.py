"""Tests for the quiz engine."""

from engine.quiz import Question, FillInQuestion, ScenarioQuestion


def test_question_construction():
    q = Question("test?", ["a", "b", "c"], 1, "expl", "beginner", "hint")
    assert q.correct == 1
    assert len(q.choices) == 3


def test_fill_in_case_normalization():
    fq = FillInQuestion("test", ["/Model", "/MODEL", "ESC"])
    assert "/model" in fq.answers
    assert "esc" in fq.answers


def test_scenario_question():
    sq = ScenarioQuestion("scene", "q?", ["a", "b"], 0)
    assert sq.correct == 0
    assert sq.scenario == "scene"
