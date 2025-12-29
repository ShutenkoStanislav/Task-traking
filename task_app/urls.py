from django.urls import path
from task_app import views


app_name = "tasks"

urlpatterns = [
    path('', views.TaskListView.as_view(), name="task_list"),
    path('<int:pk>/', views.TaskDetailView.as_view(), name="task_detail"),
    path('task-create/', views.TaskCreateView.as_view(), name="task-create"),
    path('task/<int:pk>/complete/', views.TaskCompleteView.as_view(), name="task-complete")
    
]

