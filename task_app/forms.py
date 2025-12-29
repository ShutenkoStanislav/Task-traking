from django import forms
from task_app.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date"]  


class TaskFilterForm(forms.Form):
        STATUS_CHOICES = [
        ("", "All"),
        ("todo", "To Do"),
        ("in_progress", "In progress"),
        ("done", "Done"),
        ]
        
        status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Status")
