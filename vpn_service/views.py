import requests
import sys
from urllib.parse import urlparse, urljoin
from uuid import uuid4
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Page, Redirection
from .forms import PageForm
from .parser import parser


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {"pages": Page.objects.filter(user=request.user)}

    return render(request, template_name="index.html", context=context)


@login_required
def open_with_vpn(request: HttpRequest, origin: str, route: str = "") -> HttpResponse:
    user = request.user
    page = get_object_or_404(Page, title=origin, user=user)
    page_url = page.original_url

    if route:
        page_url = urljoin(page.original_url, route)

    parsed_page = parser(
        requests.get(page_url).content,
        origin,
        route
    )
    Redirection.objects.create(
        page=page,
        uploaded_data=sys.getsizeof(request),
        downloaded_data=sys.getsizeof(parsed_page),
        route=route
    )

    return HttpResponse(parsed_page)


class PageCreateView(LoginRequiredMixin, generic.CreateView):
    model = Page
    form_class = PageForm
    template_name = "vpn_service/page_create.html"
    success_url = reverse_lazy("vpn-service:home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class PageDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Page
    template_name = "vpn_service/page_confirm_delete.html"
    success_url = reverse_lazy("vpn_service:home")
