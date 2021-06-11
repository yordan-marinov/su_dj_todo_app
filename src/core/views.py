from django.http import request
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)

from core.models import Task


class CustomLoginView(LoginView):
    template_name = "core/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy("tasks")


class RegisterPage(FormView):
    template_name = "core/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy("tasks")
    
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('task')
        return super(RegisterPage, self).get(*args, **kwargs)


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['tasks'] -> queryset of all instances of Task model
        # print(f'THIS IS THE CONTEXT -> {context["tasks"]}')
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        
        search_input = self.request.GET.get('search_area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__istartswith=search_input
            )
            
        context['search_input'] = search_input
        
        return context


# LoginRequiredMixin deny access to the view if user is not logde in
# redirect to login page
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    # To change the html name to task.html we are using:
    # template_name = "core.task.html after we rename the html file"
    # by default is looking for name task_detail.html

    # This is renaming 'object' in task_detail.html to 'task'
    context_object_name = "task"


# LoginRequiredMixin deny access to the view if user is not logde in
# redirect to login page
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    # It shows Todo's of the user who is loged in
    def form_valid(self, form):
        # print(f'This is FORM.INSTANCE.USER -> {form.instance.user}')
        # print(f'This is SELF.REQUEST.USER -> {self.request.user}')
        form.instance.user = self.request.user
        return super(TaskCreateView, self).form_valid(form)


# LoginRequiredMixin deny access to the view if user is not logde in
# redirect to login page
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")


# LoginRequiredMixin deny access to the view if user is not logde in
# redirect to login page
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    # template_name = "TEMPLATE_NAME"
    success_url = reverse_lazy("tasks")
    context_object_name = "task"
