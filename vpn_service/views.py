from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from .models import Page, Redirection
from .forms import PageForm


@login_required
def index(request: HttpRequest) -> HttpResponse:
    context = {"pages": Page.objects.filter(user=request.user)}

    return render(request, template_name="index.html", context=context)


@login_required
def open_with_vpn(request: HttpRequest) -> HttpResponse:
    pass


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
