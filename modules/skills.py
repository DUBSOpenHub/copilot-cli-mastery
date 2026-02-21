"""Module 5: Skills System — capabilities and catalogs."""

from engine.ui import (
    C, hr_fancy, print_tip, pause, info_box, menu, print_difficulty, type_text
)
from engine.quiz import Question, ScenarioQuestion, run_quiz, run_scenario


def run_lesson(progress):
    """Run the skills training module."""
    progress.visit_section("skills")

    while True:
        hr_fancy("🎨 Module 5: Skills System", C.BRIGHT_CYAN)
        print(f"\n  {C.WHITE}Skills extend the AI's capabilities with specialized knowledge.{C.RESET}\n")

        result = menu([
            ("🎓 Guided Lesson: Understanding Skills", "lesson"),
            ("🎓 Guided Lesson: Creating Custom Skills", "lesson_create"),
            ("🎯 Quiz: Skills Knowledge", "quiz"),
            ("🧩 Scenario: Skill Selection", "scenario"),
        ], "Choose activity")

        if result is None or result == "quit":
            return
        elif result == "lesson":
            _lesson(progress)
        elif result == "lesson_create":
            _lesson_create(progress)
        elif result == "quiz":
            _run_quiz(progress)
        elif result == "scenario":
            _run_scenario(progress)


def _lesson(progress):
    hr_fancy("🎓 Understanding Skills", C.BRIGHT_GREEN)
    print_difficulty("intermediate")

    type_text("\n  Skills are specialized capabilities that enhance what the AI can do.", color=C.WHITE)
    pause()

    info_box("What Are Skills?", f"""Skills are packages of knowledge and capability that the AI can invoke.

{C.GREEN}Think of them as:{C.RESET}
  • Specialized "apps" the AI can use
  • Domain-specific expertise modules
  • Pre-built workflows for common tasks

{C.YELLOW}Examples of skills:{C.RESET}
  • PDF processing — read and analyze PDF documents
  • XLSX handling — work with Excel spreadsheets
  • Code review — specialized review workflows
  • Security audit — check repository security posture
  • Custom analysis — domain-specific analysis patterns""")
    pause()

    info_box("The /skills Command", f"""{C.GREEN}/skills{C.RESET}              — list all available skills
{C.GREEN}/skills <name>{C.RESET}       — invoke a specific skill

{C.YELLOW}Skill sources:{C.RESET}
  • Built-in skills (ship with the CLI)
  • Agent-defined skills (in agent config files)
  • Organization skills (shared across teams)

{C.CYAN}Skill invocation:{C.RESET}
  When you describe a task, the AI checks if any skill
  matches your request and automatically suggests using it.
  You can also invoke skills directly.""")
    pause()

    info_box("Skill Catalogs", f"""Skills are organized in catalogs for discovery:

{C.GREEN}Browsing:{C.RESET}
  /skills shows a list with:
  • Skill name
  • Description
  • Source (built-in, agent, custom)
  • Whether it's currently active

{C.YELLOW}Auto-matching:{C.RESET}
  The AI will suggest relevant skills based on your task.
  Example: Ask about a PDF → AI suggests the PDF skill.

{C.CYAN}Priority:{C.RESET}
  When both a built-in and custom skill match,
  the custom/specialized skill takes precedence.""")
    pause()

    progress.complete_lesson("skills_basics")
    progress.check_module_achievements()


def _lesson_create(progress):
    hr_fancy("🎓 Creating Custom Skills", C.BRIGHT_GREEN)
    print_difficulty("advanced")

    type_text("\n  Build your own skills to extend the AI's powers.", color=C.WHITE)
    pause()

    info_box("Defining Skills in Agent Files", f"""Skills are defined within agent configuration files.

{C.GREEN}In your agent .md file, add a skill section:{C.RESET}

```markdown
---
name: my-agent
description: My custom agent
skills:
  - name: analyze-deps
    description: Analyze project dependencies for issues
  - name: gen-api-docs
    description: Generate API documentation from code
---

## Skills

### analyze-deps
When invoked, scan package.json/requirements.txt for:
- Outdated dependencies
- Known vulnerabilities
- Unused packages
- Version conflicts

### gen-api-docs
When invoked, scan source code for:
- REST endpoints
- GraphQL schemas
- Generate OpenAPI spec
```""")
    pause()

    info_box("Skill Design Best Practices", f"""{C.GREEN}1. Clear description:{C.RESET}
   Write a description that helps the AI match tasks to your skill.
   Bad:  "does stuff with code"
   Good: "analyzes Python test coverage and identifies untested paths"

{C.GREEN}2. Focused scope:{C.RESET}
   Each skill should do ONE thing well.
   Don't create a "do everything" skill.

{C.GREEN}3. Include instructions:{C.RESET}
   Specify exactly how the skill should operate,
   what tools to use, and what output to produce.

{C.GREEN}4. Test thoroughly:{C.RESET}
   Use /skills to verify your skill appears.
   Invoke it and check the results.""")
    pause()

    progress.complete_lesson("skills_create")
    progress.complete_lesson("skills")
    progress.check_module_achievements()


def _run_quiz(progress):
    questions = [
        Question(
            "What is a 'skill' in the Copilot CLI context?",
            ["A keyboard shortcut", "A specialized capability the AI can invoke",
             "A programming language proficiency", "A user achievement"],
            1,
            "Skills are packaged capabilities — specialized tools the AI can use.",
            "beginner"
        ),
        Question(
            "How do you list all available skills?",
            ["/list-skills", "/skills", "/capabilities", "/tools"],
            1,
            "/skills lists all available skills with descriptions.",
            "beginner"
        ),
        Question(
            "Where are custom skills defined?",
            ["In a separate skills.json file", "Within agent configuration (.md) files",
             "In the CLI settings", "In environment variables"],
            1,
            "Skills are defined as part of agent configuration in .md files.",
            "intermediate"
        ),
        Question(
            "When both a built-in and custom skill match a task, which takes priority?",
            ["Built-in always wins", "Custom/specialized skill takes priority",
             "User is asked to choose", "Most recently added wins"],
            1,
            "Custom skills take precedence — they're more specific to your needs.",
            "intermediate"
        ),
        ScenarioQuestion(
            "You frequently need to analyze Terraform configurations for security issues "
            "across multiple projects. Currently, you describe the analysis every time.",
            "What's the best approach?",
            ["Keep describing it each time",
             "Create a custom skill in a user-level agent",
             "Write a shell script instead",
             "Use the built-in security audit"],
            1,
            "A custom skill in ~/.copilot/agents/ makes it available everywhere.",
            "advanced"
        ),
    ]
    run_quiz(questions, progress, "skills", "Skills System Quiz")


def _run_scenario(progress):
    scenario = {
        "id": "skill_workflow",
        "title": "Building a Custom Skill",
        "description": "Walk through the process of creating and using\n"
                       "a custom skill for your team.",
        "difficulty": "advanced",
        "steps": [
            {
                "prompt": "Where should you define a skill that your whole team needs?",
                "options": [
                    "~/.copilot/agents/team-skill.md",
                    ".github/agents/team-skill.md",
                    "skills/team-skill.json",
                    "package.json"
                ],
                "correct": 1,
                "success_msg": "✓ .github/agents/ is shared with the whole team via git!",
                "fail_msg": ".github/agents/ makes skills available to all repo contributors.",
                "explanation": "User-level is personal; .github/agents/ is team-shared."
            },
            {
                "prompt": "How should a good skill description read?",
                "options": [
                    "'Does code analysis'",
                    "'Analyzes Python test coverage and identifies untested code paths'",
                    "'Skill for Python'",
                    "'Use this for testing'"
                ],
                "correct": 1,
                "success_msg": "✓ Specific descriptions help the AI match tasks to skills!",
                "fail_msg": "Be specific — the description is how the AI finds your skill.",
                "explanation": "Clear, specific descriptions improve automatic skill matching."
            },
            {
                "prompt": "After creating your skill, how do you verify it's discoverable?",
                "options": [
                    "Restart the CLI",
                    "Run /skills and look for it",
                    "Check the log files",
                    "Ask the AI if it knows about it"
                ],
                "correct": 1,
                "success_msg": "✓ /skills shows all discovered skills including yours!",
                "fail_msg": "Use /skills to verify your skill appears in the catalog.",
                "explanation": "/skills lists all available skills — verify yours is there."
            },
        ]
    }
    run_scenario(scenario, progress)
