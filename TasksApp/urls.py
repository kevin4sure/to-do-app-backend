from django.urls import path

from .views import TasksView, UpdateTaskView

urlpatterns = [
    path('',TasksView.as_view()),
    path('task/<int:pk>', UpdateTaskView.as_view())
]
