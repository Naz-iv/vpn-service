from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.urls import reverse_lazy
from .forms import SignUpForm, LoginForm, UserUpdateForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


def signup(request: HttpRequest) -> HttpResponse:
    form = SignUpForm()
    context = {
        "form": form
    }

    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            password = form.cleaned_data["password1"]

            form.cleaned_data.pop("password1")
            form.cleaned_data.pop("password2")

            user = get_user_model().objects.create_user(password=password, **form.cleaned_data)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("user:login"))
            else:
                context["message"] = "Cannot sign up with provided credentials!"
        else:
            context["form_error"] = form.errors
    return render(request, "registration/signup.html", context=context)


def custom_login(request: HttpRequest) -> HttpResponse:
    form = LoginForm()
    context = {
        "form": form
    }
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy("vpn_service:home"))
            else:
                context["message"] = "User with provided credentials not found!"
        else:
            context["form_error"] = form.errors
    return render(request, "registration/login.html", context=context)


class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = "user/profile.html"

    def get_success_url(self):
        user_id = self.request.user.id
        return reverse_lazy("user:profile", kwargs={"pk": user_id})

