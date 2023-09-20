from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect

from .models import Task, Tag
from .form import (
    TaskCreateForm,
    TaskUpdateForm
)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    queryset = Task.objects.prefetch_related("tags")

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task")
        is_completed = request.POST.get("is_completed")

        task = get_object_or_404(Task, pk=task_id)

        if is_completed == "True":
            task.is_completed = True

        elif is_completed == "False":
            task.is_completed = False

        task.save()

        return redirect("todo:task-list")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskCreateForm
    success_url = reverse_lazy("todo:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskUpdateForm
    success_url = reverse_lazy("todo:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:task-list")


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
