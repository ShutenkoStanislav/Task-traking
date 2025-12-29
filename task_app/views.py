from django.shortcuts import render
from task_app import models
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from task_app.forms import TaskForm

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/task_form.html"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    


