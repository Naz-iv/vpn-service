from django.urls import path, re_path
from .views import index, PageCreateView, open_with_vpn, PageDeleteView


urlpatterns = [
    path("", index, name="home"),
    path("create/", PageCreateView.as_view(), name="page-create"),
    path("delete/<int:pk>/", PageDeleteView.as_view(), name="page-delete"),
    path("<str:origin>/", open_with_vpn, name="vpn-open-base"),
    path("<str:origin>/<path:route>/", open_with_vpn, name="vpn-open"),

]

app_name = "vpn_service"
