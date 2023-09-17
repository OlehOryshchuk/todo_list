from datetime import date
from django import forms
from django.core.exceptions import ValidationError

from .models import Task


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(attrs={
                "type": "date",
            }
            ),
            "is_completed": forms.HiddenInput(),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        return validate_deadline(deadline)


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateInput(attrs={
                "type": "date",
            }),
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get("deadline")
        return validate_deadline(deadline)


def validate_deadline(deadline: date) -> date:
    if date.today() > deadline:
        raise ValidationError("Deadline should not be in past!")
    return deadline
