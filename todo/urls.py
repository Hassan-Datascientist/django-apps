from django.urls import path
from .views import task , hassan , add_task, get_tasks, delete_task



urlpatterns = [
    path("task/", get_tasks, name="get-tasks"),
    path("task/add/", task, name="get-add-task-page"),
    path("hassan/", hassan),
    path("add-task/", add_task, name="add-task"), 
    path("task/delete/<int:id>/", delete_task, name="delete-task")
]
