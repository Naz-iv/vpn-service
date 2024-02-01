from django.urls import path, include
from django.contrib.auth.views import LoginView
from .views import signup, custom_login, UserUpdateView, UserDetailView
from .forms import LoginForm

urlpatterns = [
    path("login/", custom_login, name="login"),
    path("signup/", signup, name="signup"),
    path("", include("django.contrib.auth.urls")),
    path("profile/<int:pk>/", UserUpdateView.as_view(), name="profile"),
    path("profile/<int:pk>/stats/", UserDetailView.as_view(), name="stats")

]

app_name = "user"
