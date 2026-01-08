from django.urls import path
from auth_system import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("singin/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout")
]