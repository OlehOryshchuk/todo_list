from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task, Tag
from .form import (
    TaskCreateForm,
    TaskUpdateForm
)


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

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

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))

        task_form = TaskUpdateForm(
            instance=task,
            data=self.request.POST
        )

        if task_form.is_valid():
            task_form.save()
            return redirect("todo:task-list")
        else:
            return render(
                self.request,
                "todo/task_form.html",
                {"form": task_form, "task": task}
            )


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
