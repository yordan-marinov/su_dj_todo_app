from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from core.models import Task


# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = "tasks"


class TaskDetailView(DetailView):
    model = Task
    # To change the html name to task.html we are using:
    # template_name = "core.task.html after we rename the html file"
    # by default is looking for name task_detail.html

    # This is renaming 'object' in task_detail.html to 'task'
    context_object_name = "task"


class TaskCreateView(CreateView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdateView(UpdateView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskDeleteView(DeleteView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"
