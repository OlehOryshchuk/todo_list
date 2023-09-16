from django.urls import path

from .views import (
    TaskListView,
    TaskCreateView,
    # TaskUpdateView,
    # TaskDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("task/create", TaskCreateView.as_view(), name="task-create")
]
app_name = "todo"
