from django.test import TestCase
from datetime import date

from ..models import Tag, Task


class ModelTest(TestCase):

    def setUp(self) -> None:
        self.task = Task.objects.create(
            name="MainTask",
            description="This is the main task",
            deadline=date.today(),
        )
        self.tag = Tag.objects.create(name="MainTag")

    def test_task_string_representation(self):
        self.assertEqual(str(self.task), f"{self.task.name}")
