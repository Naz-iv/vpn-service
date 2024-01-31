from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import signup, login
from .forms import LoginForm

urlpatterns = [
    path("login/", login, name="login"),
    path("signup/", signup, name="signup"),
    path("", include("django.contrib.auth.urls")),

]

app_name = "user"
