"""
Management command: python manage.py seed_fastapi_snippets

Parses the FastAPI Quarto slideshow (fastapi.qmd) and creates:
  - 2 categories  (Core, Advanced)
  - 18 CodeSnippet entries — one per slide that contains Python code

Safe to run multiple times — existing entries are skipped (get_or_create).

Usage:
  python manage.py seed_fastapi_snippets
  python manage.py seed_fastapi_snippets --file /path/to/fastapi.qmd
  python manage.py seed_fastapi_snippets --clear
"""

import re
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from typing_practice.models import Category, CodeSnippet

# ---------------------------------------------------------------------------
# Defaults
# ---------------------------------------------------------------------------
DEFAULT_QMD_PATH = (
    Path(__file__).resolve().parents[5]
    / "Videos" / "PYTHON" / "DSA" / "YT" / "02_linkedlist" / "slideshow"
    / "fastapi.qmd"
)

_SLIDE_TITLE = re.compile(r'^##\s+(.+?)(?:\s*\{[^}]*\})?\s*$', re.MULTILINE)
_CODE_BLOCK  = re.compile(r'```python\n(.*?)```', re.DOTALL)

MAX_CODE_LEN = 3500

# Titles that belong in the Core category; everything else goes to Advanced.
CORE_TITLES = {
    "Your First FastAPI App",
    "Path Operations & Routing",
    "Path, Query & Header Parameters",
    "Pydantic Schemas",
    "Pydantic Validation Pipeline",
    "Response Models & Status Codes",
    "Dependency Injection",
}

CATEGORIES = [
    {
        "name":        "FastAPI: Core",
        "slug":        "fastapi-slides-core",
        "difficulty":  "Medium",
        "badge":       "bg-teal-900/30 text-teal-400",
        "description": "First app, path operations, query params, Pydantic schemas, response models, and dependency injection.",
    },
    {
        "name":        "FastAPI: Advanced",
        "slug":        "fastapi-slides-advanced",
        "difficulty":  "Hard",
        "badge":       "bg-cyan-900/30 text-cyan-400",
        "description": "OAuth2/JWT, async SQLAlchemy, Alembic, async/await, background tasks, middleware, WebSockets, testing, and settings.",
    },
]


def _truncate(code: str) -> str:
    if len(code) <= MAX_CODE_LEN:
        return code
    trimmed = code[:MAX_CODE_LEN]
    cut = trimmed.rfind('\n\n')
    if cut > MAX_CODE_LEN // 2:
        trimmed = trimmed[:cut]
    return trimmed.rstrip() + "\n\n# ... (trimmed for typing practice)"


def parse_slides(qmd_text: str) -> list[dict]:
    slides = qmd_text.split("\n---\n")
    results = []
    seq = 0

    for slide in slides:
        title_match = _SLIDE_TITLE.search(slide)
        if not title_match:
            continue
        raw_title = title_match.group(1).strip()

        code_blocks = _CODE_BLOCK.findall(slide)
        if not code_blocks:
            continue

        if len(code_blocks) == 1:
            code = code_blocks[0].rstrip()
        else:
            code = "\n\n# ────────────────────────────────────────────────\n\n".join(
                b.rstrip() for b in code_blocks
            )

        code = _truncate(code.strip())

        seq += 1
        category_name = CATEGORIES[0]["name"] if raw_title in CORE_TITLES else CATEGORIES[1]["name"]
        difficulty    = CATEGORIES[0]["difficulty"] if raw_title in CORE_TITLES else CATEGORIES[1]["difficulty"]

        results.append({
            "seq":           seq,
            "title":         f"S{seq:02d}: {raw_title}",
            "code":          code,
            "difficulty":    difficulty,
            "category_name": category_name,
        })

    return results


class Command(BaseCommand):
    help = "Seed FastAPI slideshow snippets from fastapi.qmd."

    def add_arguments(self, parser):
        parser.add_argument(
            "--file",
            default=str(DEFAULT_QMD_PATH),
            help="Path to fastapi.qmd",
        )
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing FastAPI slide categories/snippets before re-seeding.",
        )

    def handle(self, *args, **options):
        qmd_path = Path(options["file"])
        if not qmd_path.exists():
            raise CommandError(
                f"QMD file not found: {qmd_path}\n"
                "Pass the correct path with --file <path>"
            )

        if options["clear"]:
            names = [c["name"] for c in CATEGORIES]
            n = CodeSnippet.objects.filter(category__name__in=names).delete()[0]
            Category.objects.filter(name__in=names).delete()
            self.stdout.write(self.style.WARNING(f"Cleared {n} snippets and {len(names)} categories."))

        cat_cache: dict[str, Category] = {}
        for meta in CATEGORIES:
            cat_obj, _ = Category.objects.get_or_create(
                name=meta["name"],
                defaults={"description": meta["description"]},
            )
            cat_cache[meta["name"]] = cat_obj

        qmd_text = qmd_path.read_text(encoding="utf-8")
        slides   = parse_slides(qmd_text)

        if not slides:
            raise CommandError("No slides with Python code found — check the QMD file.")

        created = skipped = 0
        for s in slides:
            _, flag = CodeSnippet.objects.get_or_create(
                title=s["title"],
                category=cat_cache[s["category_name"]],
                defaults={
                    "code_content": s["code"],
                    "difficulty":   s["difficulty"],
                },
            )
            if flag:
                created += 1
            else:
                skipped += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Done! Parsed {len(slides)} FastAPI slides → "
                f"created {created}, skipped {skipped} already-existing snippets."
            )
        )
