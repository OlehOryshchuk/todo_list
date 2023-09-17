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
        self.assertTrue(Task.objects.get(name=form_data["name"]))

    def test_task_create_invalid_task_wrong_deadline(self):
        form_data = {
            "name": "Task1",
            "description": "This is task1",
            "deadline": date.today() - timedelta(days=1),
        }

        response = self.client.post(TASK_CREATE_URL, data=form_data)

        self.assertNotEqual(response.status_code, 302)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(name=form_data["name"])

    def test_task_create_invalid_task_without_name(self):
        form_data = {
            "description": "This is task1",
            "deadline": date.today(),
        }

        response = self.client.post(TASK_CREATE_URL, data=form_data)

        self.assertNotEqual(response.status_code, 302)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(description=form_data["description"])

    def test_task_update_task_view(self):
        form_data = {
            "name": "Main MAin Task",
            "description": "This is task1",
            "deadline": date.today(),
        }

        url = reverse("todo:task-update", args=[self.task.id])

        response = self.client.post(url, data=form_data)

        self.assertRedirects(
            response,
            reverse("todo:task-list"),
            target_status_code=200,
            status_code=302,
        )
        self.task.refresh_from_db()
        self.assertEqual(self.task.name, form_data["name"])

    def test_task_delete_view(self):
        task1 = Task.objects.create(
            name="task1",
            deadline=date.today()
        )

        url = reverse("todo:task-delete", args=[task1.id])

        response = self.client.post(url)

        self.assertRedirects(
            response,
            reverse("todo:task-list"),
            target_status_code=200,
            status_code=302,
        )
        tasks = Task.objects.all()

        self.assertNotIn(task1, tasks)


class TestTagView(TestCase):
    def setUp(self) -> None:
        self.tag = Tag.objects.create(name="MainTag")

        self.paginated_by = 5

    def test_tag_list_page(self):
        for i in range(11):
            Tag.objects.create(name=f"tag{i}")

        response = self.client.get(TAG_LIST_URL)

        tag = Tag.objects.all()[:self.paginated_by]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context.get("tag_list")),
            list(tag)
        )
        self.assertTemplateUsed(
            response,
            "todo/tag_list.html"
        )

    def test_task_create_valid_task(self):
        form_data = {
            "name": "Tag1",
        }

        response = self.client.post(TAG_CREATE_URL, data=form_data)

        self.assertRedirects(
            response,
            reverse("todo:tag-list"),
            target_status_code=200,
            status_code=302,
        )
        self.assertTrue(Tag.objects.get(name=form_data["name"]))

    def test_task_create_invalid_tag_without_name(self):
        form_data = {
            "name": ""
        }

        response = self.client.post(TAG_CREATE_URL, data=form_data)

        self.assertNotEqual(response.status_code, 302)
        with self.assertRaises(Tag.DoesNotExist):
            Tag.objects.get(name=form_data["name"])

    def test_tag_update_view(self):
        form_data = {
            "name": "Main MAin Tag",
        }

        url = reverse("todo:tag-update", args=[self.tag.id])

        response = self.client.post(url, data=form_data)

        self.assertRedirects(
            response,
            reverse("todo:tag-list"),
            target_status_code=200,
            status_code=302,
        )
        self.tag.refresh_from_db()
        self.assertEqual(self.tag.name, form_data["name"])
