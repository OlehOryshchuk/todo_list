from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Task, Tag

admin.site.unregister(Group)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_filter = ["tags"]
    list_display = [
        "name",
        "description",
        "deadline",
        "created_at",
        "is_completed",
    ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = [
        "name",
    ]
