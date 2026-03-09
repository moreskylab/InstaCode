import uuid
from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class CodeSnippet(models.Model):
    DIFFICULTY_CHOICES = [
        ("Easy", "Easy"),
        ("Medium", "Medium"),
        ("Hard", "Hard"),
    ]

    title = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="snippets"
    )
    code_content = models.TextField()
    difficulty = models.CharField(
        max_length=10, choices=DIFFICULTY_CHOICES, default="Easy"
    )

    class Meta:
        ordering = ["category", "difficulty", "title"]

    def __str__(self):
        return f"{self.title} ({self.difficulty})"


class TypingSession(models.Model):
    MODE_CHOICES = [
        ("forced", "Forced Correction"),
        ("natural", "Natural"),
    ]

    session_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    snippet = models.ForeignKey(
        CodeSnippet, on_delete=models.SET_NULL, null=True, related_name="sessions"
    )
    wpm = models.FloatField()
    accuracy = models.FloatField(help_text="Accuracy as a percentage (0–100)")
    time_taken_seconds = models.PositiveIntegerField()
    typing_mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return (
            f"Session {self.session_id} | {self.snippet} | "
            f"{self.wpm:.1f} WPM | {self.accuracy:.1f}%"
        )
