# Contributing to Copilot CLI Mastery

Thanks for your interest in improving this training tool! This guide explains how to add content and run the tests.

## Project Structure

```
mastery.py            # Entry point and main menu
engine/
  ui.py               # Terminal UI helpers (colors, menus, boxes)
  progress.py          # XP, levels, achievements, save/load
  quiz.py              # Question types and quiz runner
modules/               # 8 training modules (one per topic)
data/
  validation.py        # Curriculum coverage expectations
tests/                 # Pytest suite
```

## How to Add a New Module

1. **Create `modules/your_module.py`** with a `run_lesson(progress)` function and quiz questions.
2. **Import it in `mastery.py`** and add it to the module menu in `main()`.
3. **Update `data/validation.py`** if your module introduces new slash commands, shortcuts, or scenarios.
4. **Run tests** to verify curriculum coverage still passes.

## How to Add Quiz Questions

Each module defines its own questions. The three question types are:

- `Question(text, choices, correct_index, explanation, difficulty, hint)` — multiple choice
- `FillInQuestion(text, accepted_answers)` — free-text (case-insensitive)
- `ScenarioQuestion(scenario, text, choices, correct_index)` — situational

Answer indices are **0-based**. Questions display 1-based numbers to the user.

## Running Tests

```bash
# Quick self-test (curriculum validation)
python mastery.py --self-test

# Non-interactive CI validation (no user input)
python mastery.py --non-interactive

# Full pytest suite
pip install pytest
pytest -v
```

## Accessibility

The UI respects `NO_COLOR` environment variable and `--no-color` CLI flag per https://no-color.org. When disabled, all `C.*` color attributes return empty strings.

## Code Style

- No external dependencies (stdlib only, except pytest for testing)
- Each module follows the same pattern: `run_lesson()` → `_lesson_*()` → `_run_quiz()`
- Keep question `correct` index in bounds for the `choices` list
