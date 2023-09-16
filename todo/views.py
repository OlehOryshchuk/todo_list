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

    def get_queryset(self):
        queryset = Task.objects.prefetch_related("tags")

        is_completed = self.request.GET.get("is_completed")
        task = self.request.GET.get("task")

        update_task = Task.objects.filter(id=task).first()

        if update_task:
            if is_completed == "True":
                update_task.is_completed = True
            elif is_completed == "False":
                update_task.is_completed = False

            update_task.save()

        return queryset


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
