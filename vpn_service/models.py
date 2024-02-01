from django.db import models
from django.contrib.auth import get_user_model
from urllib.parse import urlparse, urljoin


class Page(models.Model):
    original_url = models.URLField()
    title = models.CharField(max_length=128)
    user = models.ForeignKey(
        get_user_model(), related_name="pages", on_delete=models.CASCADE
    )


    class Meta:
        unique_together = ["original_url", "title", "user"]

    def __str__(self) -> str:
        return self.title


class Redirection(models.Model):
    page = models.ForeignKey(
        Page, related_name="redirections", on_delete=models.SET_NULL, null=True
    )
    datetime = models.DateTimeField(auto_now_add=True)
    uploaded_data = models.DecimalField(
        default=0, decimal_places=2, max_digits=15
    )
    downloaded_data = models.DecimalField(
        default=0, decimal_places=2, max_digits=15
    )
    route = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"Redirected to {self.page.title} at {self.datetime}"
