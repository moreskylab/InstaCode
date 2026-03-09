"""
Management command: python manage.py seed_dsa_questions

Parses the 99-question Python DSA interview markdown file (Q101–Q199) and creates:
  - 4 categories  (Foundations, Core DS, Advanced DS & Graphs, Expert Algorithms)
  - Up to 99 CodeSnippet entries (one per question)

Safe to run multiple times – existing entries are skipped (get_or_create).

Usage:
  python manage.py seed_dsa_questions
  python manage.py seed_dsa_questions --file /path/to/file.md
  python manage.py seed_dsa_questions --clear
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
    / "python_dsa_100_questions_and_answers.md"
)

# Category mapping by question-number range
CATEGORIES = [
    {
        "name": "DSA Interview: Foundations",
        "q_range": range(101, 116),     # Q101–Q115
        "difficulty": "Easy",
        "description": "Big-O, arrays, linked lists, stacks, queues, hash tables, binary trees, BST, heaps, graphs, sorting, binary search, strings.",
    },
    {
        "name": "DSA Interview: Core Patterns",
        "q_range": range(116, 136),     # Q116–Q135
        "difficulty": "Medium",
        "description": "Dynamic programming fundamentals, backtracking, advanced DP, greedy, Union-Find, segment trees, bit manipulation, math algorithms.",
    },
    {
        "name": "DSA Interview: Advanced",
        "q_range": range(136, 161),     # Q136–Q160
        "difficulty": "Medium",
        "description": "Complex algorithmic problems, randomized algorithms, matrix, intervals, palindromes, monotonic queues, tree construction, NP-complete.",
    },
    {
        "name": "DSA Interview: Expert",
        "q_range": range(161, 200),     # Q161–Q199
        "difficulty": "Hard",
        "description": "Network flow, advanced DP, self-balancing trees, hashing, computational geometry, distributed systems, streaming, game theory.",
    },
]

_Q_HEADING = re.compile(r'^###\s+Q(\d+)\.\s+(.+)', re.MULTILINE)
_CODE_BLOCK = re.compile(r'```python\n(.*?)```', re.DOTALL)

MAX_CODE_LEN = 3500


def _find_category(q_num: int) -> dict | None:
    for cat in CATEGORIES:
        if q_num in cat["q_range"]:
            return cat
    return None


def parse_questions(md_text: str) -> list[dict]:
    questions = []
    matches = list(_Q_HEADING.finditer(md_text))

    for idx, m in enumerate(matches):
        q_num = int(m.group(1))
        if not (101 <= q_num <= 199):
            continue

        title = m.group(2).strip()
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(md_text)
        section = md_text[start:end]

        code_match = _CODE_BLOCK.search(section)
        if not code_match:
            continue

        code = code_match.group(1).rstrip()

        if len(code) > MAX_CODE_LEN:
            trimmed = code[:MAX_CODE_LEN]
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


class Command(BaseCommand):
    help = "Seed 99 Python DSA interview Q&A snippets (Q101–Q199) from the markdown source file."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(DEFAULT_MD_PATH),
            help="Path to python_dsa_100_questions_and_answers.md",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete DSA interview categories/snippets before re-seeding.",
        )

    def handle(self, *args, **options):
        md_path = Path(options["file"])
        if not md_path.exists():
            raise CommandError(
                f"Markdown file not found: {md_path}\n"
                "Pass the correct path with --file <path>"
            )

        if options["clear"]:
            names = [c["name"] for c in CATEGORIES]
            snippet_count = CodeSnippet.objects.filter(category__name__in=names).count()
            CodeSnippet.objects.filter(category__name__in=names).delete()
            Category.objects.filter(name__in=names).delete()
            self.stdout.write(
                self.style.WARNING(
                    f"Cleared {snippet_count} snippets and {len(names)} categories."
                )
            )

        cat_cache: dict[str, Category] = {}
        for cat_meta in CATEGORIES:
            cat_obj, _ = Category.objects.get_or_create(
                name=cat_meta["name"],
                defaults={"description": cat_meta["description"]},
            )
            cat_cache[cat_meta["name"]] = cat_obj

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
