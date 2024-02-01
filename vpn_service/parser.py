from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.urls import reverse_lazy
from urllib.parse import urlparse, urljoin, urlunparse


def parser(response_content: str, origin: str, route: str) -> str:

    soup = BeautifulSoup(response_content, "html.parser", from_encoding="utf-8")

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if not href.startswith(("http://", "https://")):
            a_tag["href"] = reverse_lazy(
                "vpn-service:vpn-open",
                args=[origin, urljoin(route, href)]
            )

    return soup
