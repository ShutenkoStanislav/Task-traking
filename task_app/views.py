from django.shortcuts import render, get_object_or_404
from task_app import models
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from task_app.forms import TaskForm, TaskFilterForm, FolderForm
from task_app.mixins import UserIsOwner
from django.http import HttpResponseRedirect

class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        if status:
            queryset = queryset.filter(status=status)
        return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = TaskFilterForm(self.request.GET)
        context["task_form"] = TaskForm()
        context["folder_form"] = FolderForm()
        return context

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    context_object_name = "taskes"
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/task_form.html"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class FolderCreateView(LoginRequiredMixin, CreateView):
    model = models.Folder
    context_object_name = "folders"
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/folder_form.html"
    form_class = FolderForm
    
    
    
class TaskCompleteView(LoginRequiredMixin, UserIsOwner, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect(reverse_lazy('tasks:task_list'))
    
    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(models.Task, pk=task_id)

    
class TaskUpdateView(LoginRequiredMixin, UserIsOwner, UpdateView):
    model = models.Task
    form_class = TaskForm
    template_name = "tasks/task_update_form.html"
    success_url = reverse_lazy('tasks:task_list')

class TaskDeleteView(LoginRequiredMixin, UserIsOwner, DeleteView):
    model = models.Task
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/task_delete_form.html"
    

    

    


    


