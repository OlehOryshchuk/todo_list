from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tag
from .form import (
    TaskCreateForm,
    TaskUpdateForm
)


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm

    def get_success_url(self):
        return reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm

    def get_success_url(self):
        return reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")
