from django.contrib import admin
from django.db import models as db_models
from django import forms

from .models import Category, CodeSnippet, TypingSession


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "snippet_count")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)

    def snippet_count(self, obj):
        return obj.snippets.count()

    snippet_count.short_description = "Snippets"


class MonospacedTextarea(forms.Textarea):
    """Textarea with a monospace font for comfortable code editing."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("attrs", {})
        kwargs["attrs"].update(
            {
                "style": (
                    "font-family: 'Fira Code', 'Cascadia Code', Consolas, "
                    "'Courier New', monospace; font-size: 13px; "
                    "line-height: 1.6; tab-size: 4;"
                ),
                "rows": 30,
                "spellcheck": "false",
            }
        )
        super().__init__(*args, **kwargs)


class CodeSnippetAdminForm(forms.ModelForm):
    class Meta:
        model = CodeSnippet
        fields = "__all__"
        widgets = {
            "code_content": MonospacedTextarea(),
        }


@admin.register(CodeSnippet)
class CodeSnippetAdmin(admin.ModelAdmin):
    form = CodeSnippetAdminForm
    list_display = ("title", "category", "difficulty")
    list_filter = ("category", "difficulty")
    search_fields = ("title",)
    ordering = ("category", "difficulty", "title")


@admin.register(TypingSession)
class TypingSessionAdmin(admin.ModelAdmin):
    list_display = (
        "session_id",
        "snippet",
        "wpm",
        "accuracy",
        "time_taken_seconds",
        "typing_mode",
        "created_at",
    )
    list_filter = ("typing_mode", "created_at")
    readonly_fields = ("session_id", "created_at")
    ordering = ("-created_at",)
