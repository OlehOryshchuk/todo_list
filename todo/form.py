from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from .models import Task, Tag


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {
            "deadline": forms.DateInput(attrs={
                "type": "date",
            }
            ),
            "is_completed": forms.HiddenInput(),
            "created_at": forms.HiddenInput()
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        if date.today() > deadline:
            raise ValidationError("Deadline should not be in past!")
        return deadline
