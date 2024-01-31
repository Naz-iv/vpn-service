from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email..."}),
        required=True,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password..."}),
        required=True,
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username..."}),
        required=True,
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email..."}),
        required=True,
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter your password..."}),
        required=True,
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Repeat your password..."}),
        required=True,
    )

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]


class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(
        label="First name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your first name..."}),
        required=False,
    )
    last_name = forms.CharField(
        label="Last name",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your last name..."}),
        required=False,
    )
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your username..."}),
        required=False,
    )
    password = None

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username"]
