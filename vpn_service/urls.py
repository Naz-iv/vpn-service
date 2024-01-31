from django.urls import path
from .views import index, PageCreateView, open_with_vpn


urlpatterns = [
    path("", index, name="home"),
    path("create/", PageCreateView.as_view(), name="page-create"),
    path("open/", open_with_vpn, name="open"),
]

app_name = "vpn_service"
