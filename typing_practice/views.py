import json

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Max, Sum
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.text import slugify
from django.views import View
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator

from .models import Category, CodeSnippet, TypingSession


# ---------------------------------------------------------------------------
# Shared context: 10-week plan + 18 universal patterns (from DSA Visual Guide)
# ---------------------------------------------------------------------------

WEEKS = [
    {"num": 1,  "title": "Big-O + Arrays + Strings",          "diff": "Easy",     "topics": "Two Sum · Best Time to Buy · Valid Anagram · Group Anagrams · Encode & Decode"},
    {"num": 2,  "title": "Linked Lists + Two Pointers",        "diff": "Easy-Med",  "topics": "Merge Lists · Remove Nth Node · Reorder List · Cycle Detection · Middle"},
    {"num": 3,  "title": "Stacks + Queues + Sliding Window",   "diff": "Easy-Med",  "topics": "Min Stack · Queue via Stacks · Daily Temperatures · Sliding Window Max"},
    {"num": 4,  "title": "Hash Maps + Sets",                   "diff": "Easy-Med",  "topics": "LRU Cache · Longest Consecutive · Valid Anagram · Two Sum revisit"},
    {"num": 5,  "title": "Trees + BST + BFS/DFS",              "diff": "Medium",    "topics": "Level-Order BFS · Zigzag · Max Depth · Diameter · Validate BST · LCA"},
    {"num": 6,  "title": "Heaps + Top-K + Two Heaps",          "diff": "Med-Hard",  "topics": "heapq patterns · Kth Largest (3 approaches) · K Frequent · Median Stream"},
    {"num": 7,  "title": "Graphs + BFS/DFS/Topo Sort",         "diff": "Medium",    "topics": "Graph representations · Islands · Clone Graph · Pacific Atlantic · Course Schedule"},
    {"num": 8,  "title": "Binary Search Patterns",             "diff": "Easy-Hard", "topics": "3 BS templates · Sqrt(x) · Search Rotated · First/Last Position · Median of 2 Arrays"},
    {"num": 9,  "title": "Dynamic Programming",                "diff": "Med-Hard",  "topics": "Coin Change (brute→memo→DP) · LIS · Knapsack · Unique Paths · LCS · Word Break"},
    {"num": 10, "title": "Greedy + Backtracking + Revisions",  "diff": "Med-Hard",  "topics": "Activity Selection · Dijkstra · Combo Sum · Word Search · N-Queens · Full review"},
]

PATTERNS_18 = [
    {"name": "Two Pointers",            "signal": "Pair/triplet in sorted array, palindrome",      "examples": ["Two Sum II", "3-Sum", "Container WMW"]},
    {"name": "Sliding Window",          "signal": "Contiguous subarray or substring",              "examples": ["Max Sum K", "Longest No-Repeat", "Min Window"]},
    {"name": "Prefix Sum",              "signal": "Range sum, sub-array sum equals k",             "examples": ["Range Sum Query", "Sub-array Eq K"]},
    {"name": "Monotonic Stack",         "signal": "Next greater/smaller, histogram",               "examples": ["Daily Temps", "Largest Rect", "Next Greater"]},
    {"name": "Top-K Elements",          "signal": "K largest/smallest/frequent",                  "examples": ["K Frequent", "Kth Largest", "K Closest"]},
    {"name": "Fast & Slow Pointers",    "signal": "Linked list cycle, middle, duplicate",          "examples": ["Cycle Detect", "Middle Node", "Find Dup"]},
    {"name": "In-place List Reversal",  "signal": "Reverse sublist, group in k",                  "examples": ["Reverse LL", "Reverse Sub-list", "Group K"]},
    {"name": "Tree BFS (Level Order)",  "signal": "Level-by-level, shortest path in tree",        "examples": ["Level Order", "Zigzag", "Right View"]},
    {"name": "Tree DFS",                "signal": "Pre/in/post-order, paths, depth",              "examples": ["Max Depth", "LCA", "Path Sum", "Serialize"]},
    {"name": "Topological Sort",        "signal": "Dependency ordering, course schedule",         "examples": ["Course Sched", "Alien Dict", "Parallel Tasks"]},
    {"name": "Union-Find",              "signal": "Dynamic connectivity, connected components",   "examples": ["Number of Islands", "Redundant Edge"]},
    {"name": "Modified Binary Search",  "signal": "Sorted / rotated array, answer space search",  "examples": ["Search Rotated", "BS on Answer", "Sqrt(x)"]},
    {"name": "Merge Intervals",         "signal": "Overlapping ranges, inserted intervals",       "examples": ["Merge Intervals", "Insert Interval", "Meeting Rooms"]},
    {"name": "Cyclic Sort",             "signal": "Numbers 1..n in array, missing/duplicate",    "examples": ["Find Missing", "Find All Dups", "First Missing"]},
    {"name": "0-1 Knapsack (DP)",       "signal": "Include/exclude decision, max value in W",    "examples": ["0-1 Knapsack", "Subset Sum", "Partition Equal"]},
    {"name": "Two Heaps",               "signal": "Running median, schedule by two priorities",  "examples": ["Median Stream", "Sliding Win Median"]},
    {"name": "K-way Merge",             "signal": "Merge K sorted lists/arrays",                 "examples": ["Merge K Lists", "Smallest Range", "K Pairs"]},
    {"name": "Backtracking",            "signal": "All combinations/permutations/subsets",       "examples": ["Combo Sum", "Permutations", "N-Queens", "Sudoku"]},
]


class HomeView(LoginRequiredMixin, View):
    """Landing page: lists all categories and their snippets."""

    template_name = "typing_practice/home.html"

    TIER_SLUGS = {
        "green": [
            "big-o-arrays-strings", "arrays", "linked-lists",
            "stacks-queues", "stacks-queues-sliding-window",
            "recursion", "searching",
        ],
        "yellow": [
            "hash-maps-sets", "trees", "trees-bst-bfsdfs",
            "heaps-top-k-two-heaps", "trie", "sorting",
        ],
        "red": [
            "graphs", "graphs-bfsdfs-topo-sort", "dynamic-programming",
            "binary-search-variants", "binary-search-patterns",
            "two-pointers", "sliding-window", "fast-slow-pointers",
            "merge-intervals", "monotonic-stack", "backtracking",
            "backtracking-revisions", "prefix-sum", "top-k-elements",
            "union-find", "topological-sort", "greedy-algorithms",
            "python-collections", "interview-reference",
            "linked-lists-two-pointers",
        ],
    }

    def get(self, request):
        categories = list(Category.objects.prefetch_related("snippets").all())
        snippets = list(CodeSnippet.objects.select_related("category").all())

        # Annotate each category with a tier colour for the home page UI
        for cat in categories:
            if cat.slug in self.TIER_SLUGS["green"]:
                cat.tier = "green"
            elif cat.slug in self.TIER_SLUGS["yellow"]:
                cat.tier = "yellow"
            else:
                cat.tier = "red"

        # Build slug→tier map and propagate to snippet.category instances
        tier_map = {cat.slug: cat.tier for cat in categories}
        for snippet in snippets:
            snippet.category.tier = tier_map.get(snippet.category.slug, "red")

        return render(request, self.template_name, {
            "categories": categories,
            "snippets": snippets,
        })


@method_decorator(ensure_csrf_cookie, name="dispatch")
class PracticeView(LoginRequiredMixin, View):
    """Main typing interface for a given CodeSnippet."""

    template_name = "typing_practice/practice.html"

    def get(self, request, snippet_id):
        snippet = get_object_or_404(CodeSnippet, pk=snippet_id)
        categories = Category.objects.prefetch_related("snippets").all()
        return render(request, self.template_name, {
            "snippet": snippet,
            "categories": categories,
            # Serialise code safely for inline JS
            "code_json": json.dumps(snippet.code_content),
        })


class StatsAPIView(View):
    """
    POST /api/stats/
    Accepts JSON body:
      {
        "snippet_id": 3,
        "wpm": 47.2,
        "accuracy": 94.5,
        "time_taken_seconds": 83,
        "typing_mode": "forced"
      }
    Returns:
      { "status": "ok", "session_id": "<uuid>" }
    """

    def post(self, request):
        if not request.user.is_authenticated:
            return JsonResponse({"error": "Authentication required"}, status=401)
        try:
            data = json.loads(request.body)
        except (json.JSONDecodeError, ValueError):
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        required = {"snippet_id", "wpm", "accuracy", "time_taken_seconds", "typing_mode"}
        missing = required - data.keys()
        if missing:
            return JsonResponse({"error": f"Missing fields: {missing}"}, status=400)

        snippet = get_object_or_404(CodeSnippet, pk=data["snippet_id"])

        # Basic range validation
        try:
            wpm = float(data["wpm"])
            accuracy = float(data["accuracy"])
            time_taken = int(data["time_taken_seconds"])
        except (TypeError, ValueError):
            return JsonResponse({"error": "Numeric fields must be numbers"}, status=400)

        if not (0 <= accuracy <= 100):
            return JsonResponse({"error": "accuracy must be between 0 and 100"}, status=400)

        if data["typing_mode"] not in ("forced", "natural"):
            return JsonResponse({"error": "typing_mode must be 'forced' or 'natural'"}, status=400)

        session = TypingSession.objects.create(
            snippet=snippet,
            wpm=wpm,
            accuracy=accuracy,
            time_taken_seconds=time_taken,
            typing_mode=data["typing_mode"],
        )

        return JsonResponse({"status": "ok", "session_id": str(session.session_id)}, status=201)


class ResourcesView(LoginRequiredMixin, View):
    """Practice resources and study plan page (aligned with DSA Visual Guide)."""

    template_name = "typing_practice/resources.html"

    def get(self, request):
        return render(request, self.template_name, {
            "weeks": WEEKS,
            "patterns_18": PATTERNS_18,
        })


# ---------------------------------------------------------------------------
# Tracks — multi-topic practice tracks derived from QMD study guides
# ---------------------------------------------------------------------------

TRACKS = [
    {
        "slug": "dsa",
        "name": "DSA & Algorithms",
        "icon": "fa-solid fa-code-branch",
        "color": "brand",
        "border": "border-brand-700",
        "badge": "bg-brand-900/40 text-brand-300",
        "description": "Data structures, algorithms, complexity analysis and the 18 universal LeetCode patterns.",
        "qmd": "dsa.qmd",
        "category_slugs": [
            "big-o-arrays-strings",
            "arrays",
            "strings",
            "linked-lists",
            "linked-lists-two-pointers",
            "stacks-queues",
            "stacks-queues-sliding-window",
            "hash-maps-sets",
            "trees",
            "trees-bst-bfsdfs",
            "heaps-top-k-two-heaps",
            "graphs",
            "graphs-bfsdfstopo-sort",
            "searching",
            "sorting",
            "recursion",
            "dynamic-programming",
            "greedy-algorithms",
            "trie",
            "backtracking",
            "backtracking-revisions",
            "binary-search-patterns",
            "binary-search-variants",
            "sliding-window",
            "two-pointers",
            "prefix-sum",
            "fast-slow-pointers",
            "merge-intervals",
            "top-k-elements",
            "monotonic-stack",
            "topological-sort",
            "union-find",
            "bitwise-algorithms",
            "python-collections",
            "interview-reference",
        ],
    },
    {
        "slug": "web",
        "name": "Web Development",
        "icon": "fa-solid fa-globe",
        "color": "blue",
        "border": "border-blue-700",
        "badge": "bg-blue-900/40 text-blue-300",
        "description": "Django MVT architecture, ORM queries, CBVs, signals, and common design patterns.",
        "qmd": "django.qmd + fastapi.qmd + design_patterns.qmd",
        "category_slugs": [
            "django",
            "fastapi",
            "design-patterns",
        ],
    },
    {
        "slug": "devops",
        "name": "DevOps & Cloud",
        "icon": "fa-solid fa-server",
        "color": "orange",
        "border": "border-orange-700",
        "badge": "bg-orange-900/40 text-orange-300",
        "description": "Git workflows, Linux administration, Ansible automation, Docker, Kubernetes, and AWS/Azure/GCP.",
        "qmd": "git.qmd + rhcsa.qmd + rhce.qmd + dca.qmd + cka.qmd + cloud.qmd",
        "category_slugs": [
            "git",
            "linux-essentials",
            "ansible",
            "docker",
            "kubernetes",
            "cloud-computing",
        ],
    },
    {
        "slug": "system-design",
        "name": "System Design",
        "icon": "fa-solid fa-diagram-project",
        "color": "purple",
        "border": "border-purple-700",
        "badge": "bg-purple-900/40 text-purple-300",
        "description": "Scalability, load balancing, caching, consistent hashing, rate limiting, and distributed systems.",
        "qmd": "system_design.qmd",
        "category_slugs": [
            "system-design",
        ],
    },
    {
        "slug": "python-certs",
        "name": "Python Certifications",
        "icon": "fa-brands fa-python",
        "color": "yellow",
        "border": "border-yellow-700",
        "badge": "bg-yellow-900/40 text-yellow-300",
        "description": "PCEP fundamentals, PCAP OOP & modules, PCPP metaclasses, descriptors, and testing.",
        "qmd": "pcep.qmd + pcap.qmd + pcpp.qmd",
        "category_slugs": [
            "python-fundamentals",
            "python-oop",
        ],
    },
    {
        "slug": "data-science",
        "name": "Data Science",
        "icon": "fa-solid fa-chart-line",
        "color": "teal",
        "border": "border-teal-700",
        "badge": "bg-teal-900/40 text-teal-300",
        "description": "NumPy n-dimensional arrays, broadcasting, linear algebra, and Pandas DataFrames for data wrangling and analysis.",
        "qmd": "pandas_and_numpy.qmd",
        "category_slugs": [
            "pandas-numpy",
        ],
    },
    {
        "slug": "python-ds",
        "name": "Python Data Structures",
        "icon": "fa-solid fa-layer-group",
        "color": "indigo",
        "border": "border-indigo-700",
        "badge": "bg-indigo-900/40 text-indigo-300",
        "description": "From-scratch implementations of arrays, linked lists, stacks, queues, hash tables, and graphs — with classic interview algorithms.",
        "qmd": "arrays.qmd + linkedlist.qmd + stack_and_queues.qmd + hashtable.qmd + graphs.qmd",
        "category_slugs": [
            "array-fundamentals",
            "linked-list-fundamentals",
            "stack-queue-fundamentals",
            "hash-table-fundamentals",
            "graph-fundamentals",
        ],
    },
    {
        "slug": "interview",
        "name": "Python Interview: 100 Q&A",
        "icon": "fa-solid fa-user-tie",
        "color": "rose",
        "border": "border-rose-700",
        "badge": "bg-rose-900/40 text-rose-300",
        "description": "100 curated Python interview questions with complete answers — from fundamentals to expert-level patterns.",
        "qmd": "python_100_questions_and_answers.md",
        "category_slugs": [
            "python-interview-basics",
            "python-interview-oop-intermediate",
            "python-interview-advanced",
            "python-interview-expert",
        ],
    },
]

# Flat slug → track mapping for O(1) lookup
_SLUG_TO_TRACK: dict[str, dict] = {
    slug: track
    for track in TRACKS
    for slug in track["category_slugs"]
}


def _annotate_tier(categories):
    """Annotate category.tier using HomeView.TIER_SLUGS (reused here)."""
    tier_slugs = HomeView.TIER_SLUGS
    for cat in categories:
        if cat.slug in tier_slugs["green"]:
            cat.tier = "green"
        elif cat.slug in tier_slugs["yellow"]:
            cat.tier = "yellow"
        else:
            cat.tier = "red"
    return categories


# ---------------------------------------------------------------------------
# Playground — custom code typing test (no snippet saved)
# ---------------------------------------------------------------------------


@method_decorator(ensure_csrf_cookie, name="dispatch")
class PlaygroundView(LoginRequiredMixin, View):
    """Custom typing test: user pastes any code and practises it."""

    template_input  = "typing_practice/playground_input.html"
    template_typing = "typing_practice/playground_typing.html"

    def get(self, request):
        return render(request, self.template_input)

    def post(self, request):
        code = request.POST.get("code", "").strip()
        title = request.POST.get("title", "Custom Snippet").strip() or "Custom Snippet"
        lang  = request.POST.get("lang", "python")

        if not code:
            return render(request, self.template_input, {
                "error": "Please paste some code before starting.",
                "title_val": title,
                "lang_val":  lang,
            })

        # Truncate extremely long pastes (safety / UX)
        if len(code) > 20_000:
            code = code[:20_000]

        return render(request, self.template_typing, {
            "title":     title,
            "lang":      lang,
            "code_json": json.dumps(code),
        })


# ---------------------------------------------------------------------------
# In-app snippet manager (staff only)
# ---------------------------------------------------------------------------


class ManageSnippetView(LoginRequiredMixin, View):
    """In-app form to create new categories and snippets."""

    template_name = "typing_practice/manage_snippet.html"

    def _check_staff(self, request):
        """Return 403 response if user is not authenticated staff."""
        if not (request.user.is_authenticated and request.user.is_staff):
            return HttpResponseForbidden(
                "Access denied — staff login required. "
                '<a href="/admin/">Log in via Django admin</a>'
            )
        return None

    def get(self, request):
        forbidden = self._check_staff(request)
        if forbidden:
            return forbidden
        categories = Category.objects.order_by("name")
        recent = CodeSnippet.objects.select_related("category").order_by("-id")[:20]
        return render(request, self.template_name, {
            "categories":   categories,
            "recent":       recent,
            "difficulties": ["Easy", "Medium", "Hard"],
        })

    def post(self, request):
        forbidden = self._check_staff(request)
        if forbidden:
            return forbidden

        title      = request.POST.get("title", "").strip()
        code       = request.POST.get("code", "").strip()
        difficulty = request.POST.get("difficulty", "easy").lower().capitalize()
        cat_action = request.POST.get("cat_action", "existing")  # 'existing' | 'new'
        cat_id     = request.POST.get("category_id", "")
        new_cat_name = request.POST.get("new_category_name", "").strip()

        categories = Category.objects.order_by("name")
        recent     = CodeSnippet.objects.select_related("category").order_by("-id")[:20]

        # ── Validation ────────────────────────────────────────────────
        errors = {}
        if not title:
            errors["title"] = "Title is required."
        if not code:
            errors["code"] = "Code content is required."
        if difficulty not in ("Easy", "Medium", "Hard"):
            errors["difficulty"] = "Choose Easy, Medium, or Hard."

        category = None
        if cat_action == "new":
            if not new_cat_name:
                errors["category"] = "New category name is required."
            else:
                slug = slugify(new_cat_name)
                category, _ = Category.objects.get_or_create(
                    slug=slug, defaults={"name": new_cat_name}
                )
        else:
            if not cat_id:
                errors["category"] = "Select a category."
            else:
                try:
                    category = Category.objects.get(pk=int(cat_id))
                except (Category.DoesNotExist, ValueError):
                    errors["category"] = "Invalid category."

        if errors:
            return render(request, self.template_name, {
                "categories":   categories,
                "recent":       recent,
                "difficulties": ["Easy", "Medium", "Hard"],
                "errors":       errors,
                "form_data":    request.POST,
            })

        snippet = CodeSnippet.objects.create(
            title=title,
            category=category,
            code_content=code,
            difficulty=difficulty,
        )
        messages.success(request, f'Snippet "{snippet.title}" added to "{category.name}".')
        return redirect("typing_practice:practice", snippet_id=snippet.pk)


class TracksView(LoginRequiredMixin, View):
    """Overview of all practice tracks."""

    template_name = "typing_practice/tracks.html"

    def get(self, request):
        # Attach live counts to each track dict (shallow-copy to avoid mutation)
        enriched = []
        for track in TRACKS:
            cats = Category.objects.filter(slug__in=track["category_slugs"])
            snippet_count = CodeSnippet.objects.filter(category__in=cats).count()
            enriched.append({
                **track,
                "cat_count": cats.count(),
                "snippet_count": snippet_count,
            })
        return render(request, self.template_name, {"tracks": enriched})


class TrackDetailView(LoginRequiredMixin, View):
    """Practice home filtered to a single track."""

    template_name = "typing_practice/track_detail.html"

    def get(self, request, track_slug):
        track = next((t for t in TRACKS if t["slug"] == track_slug), None)
        if track is None:
            from django.http import Http404
            raise Http404(f"Track {track_slug!r} not found")

        categories = list(
            Category.objects.prefetch_related("snippets")
            .filter(slug__in=track["category_slugs"])
        )
        _annotate_tier(categories)
        snippets = list(
            CodeSnippet.objects.select_related("category")
            .filter(category__slug__in=track["category_slugs"])
        )
        tier_map = {cat.slug: cat.tier for cat in categories}
        for snippet in snippets:
            snippet.category.tier = tier_map.get(snippet.category.slug, "red")

        return render(request, self.template_name, {
            "track": track,
            "categories": categories,
            "snippets": snippets,
        })


class StatsHistoryView(LoginRequiredMixin, View):
    """Paginated table of all recorded typing sessions, newest first."""

    template_name = "typing_practice/stats_history.html"

    def get(self, request):
        sessions = (
            TypingSession.objects
            .select_related("snippet", "snippet__category")
            .order_by("-created_at")[:200]
        )
        return render(request, self.template_name, {"sessions": sessions})


class DashboardView(LoginRequiredMixin, View):
    """Progress & improvement dashboard aggregating all TypingSession data."""

    template_name = "typing_practice/dashboard.html"

    def get(self, request):
        # ── Overall headline stats ─────────────────────────────────────────
        overall = TypingSession.objects.aggregate(
            total_sessions=Count("id"),
            avg_wpm=Avg("wpm"),
            best_wpm=Max("wpm"),
            avg_accuracy=Avg("accuracy"),
            total_seconds=Sum("time_taken_seconds"),
        )

        # ── Per-category performance (worst avg WPM first) ─────────────────
        cat_stats = list(
            TypingSession.objects
            .filter(snippet__isnull=False)
            .values("snippet__category__name", "snippet__category__slug")
            .annotate(
                sessions=Count("id"),
                avg_wpm=Avg("wpm"),
                best_wpm=Max("wpm"),
                avg_acc=Avg("accuracy"),
            )
            .order_by("avg_wpm")
        )

        # ── Per-difficulty breakdown ───────────────────────────────────────
        diff_stats = list(
            TypingSession.objects
            .filter(snippet__isnull=False)
            .values("snippet__difficulty")
            .annotate(
                sessions=Count("id"),
                avg_wpm=Avg("wpm"),
                avg_acc=Avg("accuracy"),
            )
            .order_by("snippet__difficulty")
        )

        # ── Per-mode comparison ────────────────────────────────────────────
        mode_stats = list(
            TypingSession.objects
            .values("typing_mode")
            .annotate(
                sessions=Count("id"),
                avg_wpm=Avg("wpm"),
                avg_acc=Avg("accuracy"),
            )
        )

        # ── WPM / accuracy trend (last 50 sessions, chronological) ─────────
        trend_qs = list(
            TypingSession.objects
            .order_by("-created_at")
            .values("wpm", "accuracy", "created_at")[:50]
        )
        trend_qs.reverse()

        trend_json = json.dumps([
            {
                "wpm":  round(float(s["wpm"]), 1),
                "acc":  round(float(s["accuracy"]), 1),
                "date": s["created_at"].strftime("%b %d %H:%M"),
            }
            for s in trend_qs
        ])

        # ── Snippet completion ─────────────────────────────────────────────
        total_snippets   = CodeSnippet.objects.count()
        practiced_ids    = set(
            TypingSession.objects
            .filter(snippet__isnull=False)
            .values_list("snippet_id", flat=True)
            .distinct()
        )
        practiced_count  = len(practiced_ids)

        # ── Per-snippet bests (worst avg WPM first — needs improvement) ─────
        snippet_stats = list(
            TypingSession.objects
            .filter(snippet__isnull=False)
            .values(
                "snippet__id",
                "snippet__title",
                "snippet__category__name",
                "snippet__difficulty",
            )
            .annotate(
                sessions=Count("id"),
                best_wpm=Max("wpm"),
                avg_wpm=Avg("wpm"),
                avg_acc=Avg("accuracy"),
            )
            .order_by("avg_wpm")[:10]
        )

        # ── Chart.js JSON payloads ─────────────────────────────────────────
        cat_stats_json = json.dumps([
            {
                "name":     c["snippet__category__name"],
                "avg_wpm":  round(float(c["avg_wpm"] or 0), 1),
                "avg_acc":  round(float(c["avg_acc"] or 0), 1),
                "sessions": c["sessions"],
            }
            for c in cat_stats
        ])

        diff_json = json.dumps([
            {
                "difficulty": d["snippet__difficulty"],
                "avg_wpm":    round(float(d["avg_wpm"] or 0), 1),
                "avg_acc":    round(float(d["avg_acc"] or 0), 1),
                "sessions":   d["sessions"],
            }
            for d in diff_stats
        ])

        # ── Recent sessions for the mini-table ────────────────────────────
        recent = (
            TypingSession.objects
            .select_related("snippet", "snippet__category")
            .order_by("-created_at")[:15]
        )

        return render(request, self.template_name, {
            "overall":        overall,
            "cat_stats":      cat_stats,
            "diff_stats":     diff_stats,
            "mode_stats":     mode_stats,
            "total_snippets": total_snippets,
            "practiced_count": practiced_count,
            "snippet_stats":  snippet_stats,
            "recent":         recent,
            "trend_json":     trend_json,
            "cat_stats_json": cat_stats_json,
            "diff_json":      diff_json,
        })


# ---------------------------------------------------------------------------
# User management (staff only)
# ---------------------------------------------------------------------------


class UserManagementView(LoginRequiredMixin, View):
    """List all users — staff only."""

    template_name = "typing_practice/user_management.html"

    def _require_staff(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Staff access required.")
        return None

    def get(self, request):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden
        users = User.objects.order_by("username")
        return render(request, self.template_name, {"users": users})


class UserCreateView(LoginRequiredMixin, View):
    """Create a new user — staff only."""

    template_name = "typing_practice/user_form.html"

    def _require_staff(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Staff access required.")
        return None

    def get(self, request):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden
        return render(request, self.template_name, {"action": "Create", "form_data": {}})

    def post(self, request):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden

        username  = request.POST.get("username", "").strip()
        email     = request.POST.get("email", "").strip()
        password  = request.POST.get("password", "")
        is_staff  = request.POST.get("is_staff") == "on"
        is_active = request.POST.get("is_active", "on") == "on"

        errors = {}
        if not username:
            errors["username"] = "Username is required."
        elif User.objects.filter(username=username).exists():
            errors["username"] = "A user with this username already exists."
        if len(password) < 8:
            errors["password"] = "Password must be at least 8 characters."

        if errors:
            return render(request, self.template_name, {
                "action": "Create", "errors": errors, "form_data": request.POST,
            })

        User.objects.create_user(
            username=username, email=email, password=password,
            is_staff=is_staff, is_active=is_active,
        )
        messages.success(request, f"User \"{username}\" created successfully.")
        return redirect("typing_practice:user_list")


class UserEditView(LoginRequiredMixin, View):
    """Edit an existing user — staff only."""

    template_name = "typing_practice/user_form.html"

    def _require_staff(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Staff access required.")
        return None

    def get(self, request, user_id):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden
        user_obj = get_object_or_404(User, pk=user_id)
        return render(request, self.template_name, {
            "action": "Edit", "user_obj": user_obj, "form_data": {},
        })

    def post(self, request, user_id):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden

        user_obj  = get_object_or_404(User, pk=user_id)
        email     = request.POST.get("email", "").strip()
        is_staff  = request.POST.get("is_staff") == "on"
        is_active = request.POST.get("is_active") == "on"
        password  = request.POST.get("password", "").strip()

        errors = {}
        if password and len(password) < 8:
            errors["password"] = "Password must be at least 8 characters."

        # Prevent removing staff from yourself
        if user_obj == request.user and not is_staff:
            errors["is_staff"] = "You cannot remove staff access from your own account."

        if errors:
            return render(request, self.template_name, {
                "action": "Edit", "user_obj": user_obj, "errors": errors, "form_data": request.POST,
            })

        user_obj.email     = email
        user_obj.is_staff  = is_staff
        user_obj.is_active = is_active
        if password:
            user_obj.set_password(password)
        user_obj.save()

        messages.success(request, f"User \"{user_obj.username}\" updated.")
        return redirect("typing_practice:user_list")


class UserDeleteView(LoginRequiredMixin, View):
    """Delete a user — staff only. Cannot delete yourself."""

    template_name = "typing_practice/user_confirm_delete.html"

    def _require_staff(self, request):
        if not request.user.is_staff:
            return HttpResponseForbidden("Staff access required.")
        return None

    def get(self, request, user_id):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden
        user_obj = get_object_or_404(User, pk=user_id)
        if user_obj == request.user:
            messages.error(request, "You cannot delete your own account.")
            return redirect("typing_practice:user_list")
        return render(request, self.template_name, {"user_obj": user_obj})

    def post(self, request, user_id):
        forbidden = self._require_staff(request)
        if forbidden:
            return forbidden
        user_obj = get_object_or_404(User, pk=user_id)
        if user_obj == request.user:
            messages.error(request, "You cannot delete your own account.")
            return redirect("typing_practice:user_list")
        username = user_obj.username
        user_obj.delete()
        messages.success(request, f"User \"{username}\" deleted.")
        return redirect("typing_practice:user_list")


# ---------------------------------------------------------------------------
# Interview Q&A — 100 Python interview questions browser
# ---------------------------------------------------------------------------

INTERVIEW_CATEGORIES = [
    {"name": "Python Interview: Basics",              "slug": "python-interview-basics",             "q_range": "Q1–Q25",   "badge": "bg-green-900/30 text-green-400"},
    {"name": "Python Interview: OOP & Intermediate",  "slug": "python-interview-oop-intermediate",   "q_range": "Q26–Q50",  "badge": "bg-blue-900/30 text-blue-400"},
    {"name": "Python Interview: Advanced",            "slug": "python-interview-advanced",           "q_range": "Q51–Q76",  "badge": "bg-yellow-900/30 text-yellow-400"},
    {"name": "Python Interview: Expert",              "slug": "python-interview-expert",             "q_range": "Q77–Q100", "badge": "bg-red-900/30 text-red-400"},
]


class InterviewView(LoginRequiredMixin, View):
    """Browse and practice all 100 Python interview Q&A snippets."""

    template_name = "typing_practice/interview.html"

    def get(self, request):
        import re as _re

        def _q_num(snippet):
            m = _re.match(r'Q(\d+)', snippet.title)
            return int(m.group(1)) if m else 9999

        sections = []
        for meta in INTERVIEW_CATEGORIES:
            try:
                cat = Category.objects.get(slug=meta["slug"])
                snippets = sorted(
                    CodeSnippet.objects.filter(category=cat),
                    key=_q_num,
                )
                sections.append({**meta, "snippets": snippets, "count": len(snippets)})
            except Category.DoesNotExist:
                sections.append({**meta, "snippets": [], "count": 0})

        total = sum(s["count"] for s in sections)
        return render(request, self.template_name, {
            "sections": sections,
            "total":    total,
        })


# ---------------------------------------------------------------------------
# DSA Interview Q&A — 99 Python DSA interview questions browser (Q101–Q199)
# ---------------------------------------------------------------------------

DSA_INTERVIEW_CATEGORIES = [
    {"name": "DSA Interview: Foundations",    "slug": "dsa-interview-foundations",   "q_range": "Q101–Q115", "badge": "bg-green-900/30 text-green-400"},
    {"name": "DSA Interview: Core Patterns",  "slug": "dsa-interview-core-patterns", "q_range": "Q116–Q135", "badge": "bg-blue-900/30 text-blue-400"},
    {"name": "DSA Interview: Advanced",       "slug": "dsa-interview-advanced",      "q_range": "Q136–Q160", "badge": "bg-amber-900/30 text-amber-400"},
    {"name": "DSA Interview: Expert",         "slug": "dsa-interview-expert",        "q_range": "Q161–Q199", "badge": "bg-red-900/30 text-red-400"},
]


class DsaInterviewView(LoginRequiredMixin, View):
    """Browse and practice all 99 Python DSA interview Q&A snippets."""

    template_name = "typing_practice/dsa_interview.html"

    def get(self, request):
        import re as _re

        def _q_num(snippet):
            m = _re.match(r'Q(\d+)', snippet.title)
            return int(m.group(1)) if m else 9999

        sections = []
        for meta in DSA_INTERVIEW_CATEGORIES:
            try:
                cat = Category.objects.get(slug=meta["slug"])
                snippets = sorted(
                    CodeSnippet.objects.filter(category=cat),
                    key=_q_num,
                )
                sections.append({**meta, "snippets": snippets, "count": len(snippets)})
            except Category.DoesNotExist:
                sections.append({**meta, "snippets": [], "count": 0})

        total = sum(s["count"] for s in sections)
        return render(request, self.template_name, {
            "sections": sections,
            "total":    total,
        })

