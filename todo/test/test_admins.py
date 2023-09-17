from datetime import date, datetime
from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

from ..models import Task, Tag
from ..admin import TaskAdmin, TagAdmin


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_superuser(
            username="admin", password="admin123"
        )
        self.client.force_login(self.user)

        self.task = Task.objects.create(
            name="MainTask",
            description="This is main test",
            deadline=date.today(),
        )
        self.tag = Tag.objects.create(name="MainTag")

    def test_task_admin_site_list_page(self):
        url = reverse("admin:todo_task_changelist")

        response = self.client.get(url)

        expected_fields = [
            self.task.name,
            self.task.description,
            self.task.is_completed,
        ]

        for field in expected_fields:
            self.assertContains(response, field)

        self.assertIn("deadline", TaskAdmin.list_display)
        self.assertIn("created_at", TaskAdmin.list_display)

    def test_task_admin_list_page_search_bar(self):
        new_task = Task.objects.create(
            name="Task1",
            deadline=date.today(),
        )

        url = reverse("admin:todo_task_changelist")

        response = self.client.get(url, {"q": self.task.name})

        change_list = response.context.get("cl")

        self.assertIn(self.task, change_list.queryset)
        self.assertNotIn(new_task, change_list.queryset)

    def test_task_admin_list_page_filter_task_by_tag(self):
        tag1 = Tag.objects.create(name="Tag1")
        self.task.tags.add(tag1)

        task1 = Task.objects.create(
            name="task1",
            deadline=date.today()
        )

        url = reverse("admin:todo_task_changelist")

        response = self.client.get(url, {"tags__id__exact": tag1.id})

        changelist = response.context.get("cl")

        self.assertIn(self.task, changelist.queryset)
        self.assertNotIn(task1, changelist.queryset)
