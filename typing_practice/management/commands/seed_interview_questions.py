"""
Management command: python manage.py seed_interview_questions <path_to_md>

Parses the 100-question Python interview markdown file and creates:
  - 4 categories  (Basics, OOP & Intermediate, Advanced, Expert)
  - Up to 100 CodeSnippet entries (one per question)

Safe to run multiple times – existing entries are skipped (get_or_create).

Usage:
  python manage.py seed_interview_questions
  python manage.py seed_interview_questions --file /path/to/file.md
  python manage.py seed_interview_questions --clear
"""

import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from typing_practice.models import Category, CodeSnippet

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
DEFAULT_MD_PATH = (
    Path(__file__).resolve().parents[4]
    / "Videos" / "PYTHON" / "pdf"
    / "BOOK - python_interview"
    / "python_100_questions_and_answers.md"
)

# Category mapping by question-number range
CATEGORIES = [
    {
        "name": "Python Interview: Basics",
        "q_range": range(1, 26),       # Q1–Q25
        "difficulty": "Easy",
        "description": "Core Python concepts: data types, control flow, comprehensions, decorators, generators, scope.",
    },
    {
        "name": "Python Interview: OOP & Intermediate",
        "q_range": range(26, 51),      # Q26–Q50
        "difficulty": "Medium",
        "description": "Object-oriented programming, inheritance, magic methods, MRO, metaclasses, descriptors.",
    },
    {
        "name": "Python Interview: Advanced",
        "q_range": range(51, 77),      # Q51–Q76
        "difficulty": "Medium",
        "description": "async/await, itertools, design patterns, concurrency, functools, dataclasses, type hints.",
    },
    {
        "name": "Python Interview: Expert",
        "q_range": range(77, 101),     # Q77–Q100
        "difficulty": "Hard",
        "description": "Memory management, GIL, metaclasses deep-dive, import system, optimization, security.",
    },
]

# Match: #### Q1: title   OR   ### Q77. title
_Q_HEADING = re.compile(r'^(?:#{3,4})\s+Q(\d+)[:.]\s+(.+)', re.MULTILINE)
_CODE_BLOCK = re.compile(r'```python\n(.*?)```', re.DOTALL)

# Max chars for a single snippet (keeps typing sessions reasonable)
MAX_CODE_LEN = 3500


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------

def _find_category(q_num: int) -> dict | None:
    for cat in CATEGORIES:
        if q_num in cat["q_range"]:
            return cat
    return None


def parse_questions(md_text: str) -> list[dict]:
    """Return list of {q_num, title, code, difficulty, category_name}."""
    questions = []
    matches = list(_Q_HEADING.finditer(md_text))

    for idx, m in enumerate(matches):
        q_num = int(m.group(1))
        # Only handle Q1-Q100
        if not (1 <= q_num <= 100):
            continue

        title = m.group(2).strip()
        # Text from this heading to the next (or EOF)
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        section = md_text[start:end]

        # Find first Python code block in this section
        code_match = _CODE_BLOCK.search(section)
        if not code_match:
            continue

        code = code_match.group(1).rstrip()

        # Trim extremely long blocks at a natural boundary (blank line before limit)
        if len(code) > MAX_CODE_LEN:
            trimmed = code[:MAX_CODE_LEN]
            # Walk back to last blank line for a clean cut
            cut = trimmed.rfind('\n\n')
            if cut > MAX_CODE_LEN // 2:
                trimmed = trimmed[:cut]
            code = trimmed.rstrip() + "\n\n# ... (trimmed for typing practice)"

        cat_meta = _find_category(q_num)
        if not cat_meta:
            continue

        questions.append({
            "q_num":         q_num,
            "title":         f"Q{q_num}: {title}",
            "code":          code.strip(),
            "difficulty":    cat_meta["difficulty"],
            "category_name": cat_meta["name"],
        })

    return questions


# ---------------------------------------------------------------------------
# Command
# ---------------------------------------------------------------------------

class Command(BaseCommand):
    help = "Seed 100 Python interview Q&A snippets from the markdown source file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(DEFAULT_MD_PATH),
            help="Path to python_100_questions_and_answers.md",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete interview categories/snippets before re-seeding.",
        )

    def handle(self, *args, **options):
        md_path = Path(options["file"])
        if not md_path.exists():
            raise CommandError(
                f"Markdown file not found: {md_path}\n"
                "Pass the correct path with --file <path>"
            )

        # Optionally clear existing interview data
        if options["clear"]:
            names = [c["name"] for c in CATEGORIES]
            deleted_cats = Category.objects.filter(name__in=names)
            snippet_count = CodeSnippet.objects.filter(
                category__name__in=names
            ).count()
            CodeSnippet.objects.filter(category__name__in=names).delete()
            deleted_cats.delete()
            self.stdout.write(
                self.style.WARNING(
                    f"Cleared {snippet_count} snippets and {len(names)} categories."
                )
            )

        # Ensure categories exist with descriptions
        cat_cache: dict[str, Category] = {}
        for cat_meta in CATEGORIES:
            cat_obj, _ = Category.objects.get_or_create(
                name=cat_meta["name"],
                defaults={"description": cat_meta["description"]},
            )
            cat_cache[cat_meta["name"]] = cat_obj

        # Parse markdown
        md_text = md_path.read_text(encoding="utf-8")
        questions = parse_questions(md_text)

        if not questions:
            raise CommandError("No questions parsed — check the markdown file format.")

        created = 0
        skipped = 0

        for q in sorted(questions, key=lambda x: x["q_num"]):
            cat_obj = cat_cache[q["category_name"]]
            _, created_flag = CodeSnippet.objects.get_or_create(
                title=q["title"],
                category=cat_obj,
                defaults={
                    "code_content": q["code"],
                    "difficulty":   q["difficulty"],
                },
            )
            if created_flag:
                created += 1
            else:
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Parsed {len(questions)} questions → "
                f"created {created}, skipped {skipped} already-existing snippets."
            )
        )
