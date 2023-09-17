from datetime import date, datetime
from django.test import TestCase
from django.shortcuts import reverse

from ..form import (
    TaskUpdateForm,
    TaskCreateForm,
    validate_deadline,
)


class TaskFormTest(TestCase):

    def setUp(self) -> None:
        self.update_task_form = TaskUpdateForm()
        self.create_task_form = TaskCreateForm()

    def test_task_create_fields(self):
        expected_fields = [
            "name",
            "description",
            "deadline",
            "is_completed",
            "tags",
        ]

        self.assertEqual(
            list(self.create_task_form.fields.keys()),
            expected_fields
        )

