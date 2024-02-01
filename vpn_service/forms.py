from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    title = forms.CharField(
        label="Page title",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter page title..."}),
        required=True,
    )
    original_url = forms.CharField(
        label="Page url",
        widget=forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter page url..."}),
        required=True,
    )

    class Meta:
        model = Page
        fields = ["title", "original_url"]
