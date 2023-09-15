from django.contrib import admin

from .models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["tags"]
    list_display = [
        "name",
        "description",
        "deadline",
        "is_completed",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
    ]

