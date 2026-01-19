from django.shortcuts import render, get_object_or_404, redirect
from task_app import models
from .models import Folder
from django.views.generic import ListView, DetailView, CreateView, View, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from task_app.forms import TaskForm, TaskFilterForm, FolderForm, SinginForm, CommentForm
from task_app.mixins import UserIsOwner
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.views import LoginView, LogoutView

from django.contrib.auth import login



class TaskListView(ListView):
    model = models.Task
    context_object_name = "tasks"
    template_name = "tasks/task_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()

        folder_id = self.kwargs.get('folder_id')

        if folder_id:
            queryset = queryset.filter(folder_id=folder_id)
        else:
            queryset = queryset.filter(folder__isnull=True)
        
        status = self.request.GET.get('status')
        priority = self.request.GET.get("priority")

        if status:
            queryset = queryset.filter(status=status)
        else:
           queryset = queryset.exclude(status="done")

        if priority:
            queryset = queryset.filter(priority=priority)
        return queryset.order_by("-due_date", "-created_at")
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["folders"] = Folder.objects.all()

        folder_id = self.kwargs.get('folder_id')
        if folder_id:
            context['current_folder'] = Folder.objects.get(id=folder_id)
        else:
            context['current_folder'] = None

        context["form"] = TaskFilterForm(self.request.GET)
        context["task_form"] = TaskForm()
        context["folder_form"] = FolderForm()
        
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect("tasks:task_detail", pk=comment.task.pk)
        else:
            pass

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    context_object_name = "taskes"
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/task_form.html"
    form_class = TaskForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        folder_id = self.object.folder_id
        if folder_id:
            return reverse_lazy('tasks:folder-tasks', kwargs={'folder_id': folder_id})
        return reverse_lazy('tasks:task_list')

    
class FolderCreateView(LoginRequiredMixin, CreateView):
    model = models.Folder
    context_object_name = "folders"
    success_url = reverse_lazy('tasks:task_list')
    template_name = "tasks/folder_form.html"
    form_class = FolderForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

  
    
class TaskCompleteView(LoginRequiredMixin, UserIsOwner, View):
    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return JsonResponse({'status': 'success'})
    
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
    
class CustomLoginView(LoginView):
    template_name = "auth/login.html"
    redirect_authenticated_user = True
        

    
class CustomLogoutView(LogoutView):
    next_page = "tasks:login"

class RegisterViews(CreateView):
    template_name = "auth/singin.html"
    form_class = SinginForm
   

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("tasks:login")

    


