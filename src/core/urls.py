from django.urls import path

from .views import TaskDeleteView, TaskList, TaskDetailView, TaskCreateView, TaskUpdateView

urlpatterns = [
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task"),
    path("new/", TaskCreateView.as_view(), name="new"),
    path("edit/<int:pk>", TaskUpdateView.as_view(), name="edit"),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),
]
