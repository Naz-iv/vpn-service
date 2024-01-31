from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("user.urls", namespace="user"))
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
