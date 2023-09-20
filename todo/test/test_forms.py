from datetime import date, timedelta
from django.test import TestCase
from django.core.exceptions import ValidationError

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

    def test_task_create_form_fields_widgets(self):
        rendered_form = self.create_task_form.as_table()

        self.assertIn('type="date"', rendered_form)
        self.assertIn('type="hidden" name="is_completed"', rendered_form)

    def test_task_update_form_fields(self):
        expected_fields = [
            "name",
            "description",
            "deadline",
            "is_completed",
            "tags",
        ]

        self.assertEqual(
            list(self.update_task_form.fields.keys()),
            expected_fields
        )

    def test_task_update_form_fields_widgets(self):
        rendered_form = self.update_task_form.as_table()

        self.assertIn('type="date"', rendered_form)
        self.assertIn('type="checkbox" name="is_completed"', rendered_form)

    def test_task_validate_deadline_function_in_future(self):
        future_date = date.today() + timedelta(days=1)

        result = validate_deadline(future_date)

        self.assertEqual(result, future_date)

    def test_task_validate_deadline_function_in_past(self):
        past_date = date.today() - timedelta(days=1)

        with self.assertRaises(ValidationError):
            validate_deadline(past_date)

    def test_task_validate_deadline_function_date_today(self):
        today_date = date.today()

        result = validate_deadline(today_date)

        self.assertEqual(result, today_date)
