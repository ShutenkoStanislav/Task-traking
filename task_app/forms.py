from django import forms
from task_app.models import Task, Folder

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "due_date", "folder"] 
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})

        self.fields['due_date'].widget.attrs["class"] += " my-custom=datepicker"

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["name", "color"]
    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        for fielde in self.fields:
            self.fields[fielde].widget.attrs.update({"class": "form-control"})
        self.fields["color"].widget.attrs.update({"class": "form-select"})
            




            
                 


class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
    ("", "All"),
    ("todo", "To Do"),
    ("in_progress", "In progress"),
    ("done", "Done"),
    ]
        
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=False, label="Status")

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({"class": "form-select"})

   
    