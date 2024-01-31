from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = LoginForm()
    return render(request, "registration/login.html", {"form": form})
