from django.urls import path

from .views import (
    index,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)

urlpatterns = [
    path("/", index, name="index")
]
app_name = "todo"
