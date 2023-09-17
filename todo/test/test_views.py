from django.test import TestCase
from django.shortcuts import reverse
from django.urls import reverse_lazy
from datetime import date, timedelta

from ..models import Tag, Task

TASK_LIST_URL = reverse_lazy("todo:task-list")
TASK_CREATE_URL = reverse_lazy("todo:task-create")

TAG_LIST_URL = reverse_lazy("todo:tag-list")
TAG_CREATE_URL = reverse_lazy("todo:tag-create")


class TaskViewTest(TestCase):
    def setUp(self) -> None:
        self.task = Task.objects.create(
            name="MainTask",
            description="This is the main task",
            deadline=date.today()
        )
        self.paginated_by = 5

    def test_task_list_page(self):
        for i in range(11):
            Task.objects.create(
                name=f"Task{i}",
                deadline=date.today(),
            )

        response = self.client.get(TASK_LIST_URL)

        tasks = Task.objects.all()[:self.paginated_by]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context.get("task_list")),
            list(tasks)
        )
        self.assertTemplateUsed(
            response,
            "todo/task_list.html"
        )

    def test_task_create_valid_task(self):
        form_data = {
            "name": "Task1",
            "description": "This is task1",
            "deadline": date.today(),
        }

        response = self.client.post(TASK_CREATE_URL, data=form_data)

        self.assertRedirects(
            response,
            reverse("todo:task-list"),
            target_status_code=200,
            status_code=302,
        )

    def test_task_create_invalid_task_wrong_deadline(self):
        form_data = {
            "name": "Task1",
            "description": "This is task1",
            "deadline": date.today() - timedelta(days=1),
        }

        response = self.client.post(TASK_CREATE_URL, data=form_data)

        self.assertNotEqual(response.status_code, 302)

    def test_task_create_invalid_task_without_name(self):
        form_data = {
            "description": "This is task1",
            "deadline": date.today(),
        }

        response = self.client.post(TASK_CREATE_URL, data=form_data)

        self.assertNotEqual(response.status_code, 302)
