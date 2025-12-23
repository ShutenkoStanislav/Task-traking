from django.shortcuts import render
from task_app import models
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"

class TaskCreateView(CreateView):
    model = models.Task
    success_url = reverse_lazy('task_list')
    template_name = "tasks/task_form.html"
    form_class = Taskform
    


