from django.shortcuts import render, redirect
from auth_system.form import LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("task_list")
        

    else:
        form = LoginForm()
        messages.error(request, "Invalid respond data")

    return render(
        request,
        template_name="auth_systems/singin.html",
        context= {'form' : form},
    )

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(
            request,
            data=request.POST,
            )
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request,
                                username=username,
                                password=password
                        )
            if user is not None:
                auth_login(request, user)
                return redirect("task_list")
            else:
                messages.error(request, "Incorrect login or password")
        else:
            messages.error(request, "Invalid data for form")

    else:
        form = AuthenticationForm()
    return render(request, "auth_systems/login.html", {'form' : form})

