from django.contrib.auth.forms import UserCreationForm
from task_app.models import Task

class LoginForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Task
        fields = UserCreationForm.Meta.fields = ("first_name", "last_name", "email", "username")
        
