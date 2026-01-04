from django import forms
from task_app.models import Task, Folder

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "priority", "due_date", "folder"] 
        widgets = {
            'due_date': forms.DateInput(attrs={
                "class": "form-control transparent-input",
                "placeholder" : "Date",
                "type": "date"
            })
        }
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({
            "class": "form-control noborder-input title-input",
            "placeholder" : "Title"
        })

        self.fields['description'].widget.attrs.update({
            "class": "form-control noborder-input content-input",
            "placeholder" : "Content"
        })

       
    

        self.fields['priority'].widget.attrs.update({
            "class": "form-control transparent-input",
            "placeholder" : "Priority"
            
        })

        self.fields['folder'].widget.attrs.update({
            "class": "form-control transparent-input",
            "placeholder" : "Folder",
            
        })

        

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ["name", "color"]
    def __init__(self, *args, **kwargs):
        super(FolderForm, self).__init__(*args, **kwargs)
        
            
        self.fields['name'].widget.attrs.update({
            "class": "form-control noborder-input content-input",
            "placeholder" : "Name"
        })

        self.fields['color'].widget.attrs.update({
            "class": "form-control transparent-input",
            "placeholder" : "Color"
            
        })
            




            
                 


class TaskFilterForm(forms.Form):
    PRIORITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
                ]
        
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, required=False, label="Priority")

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        self.fields['priority'].widget.attrs.update({"class": "form-select"})

   
    