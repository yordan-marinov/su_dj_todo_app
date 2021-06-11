from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import (
    CustomLoginView,
    RegisterPage,
    TaskDeleteView,
    TaskList,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
)


urlpatterns = [
    # Login and Logout logic as you are logout will be redirected to login page
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),
    # Register page
    path("register/", RegisterPage.as_view(), name="register"),
    
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetailView.as_view(), name="task"),
    path("new/", TaskCreateView.as_view(), name="new"),
    path("edit/<int:pk>", TaskUpdateView.as_view(), name="edit"),
    path("delete/<int:pk>", TaskDeleteView.as_view(), name="delete"),
]
