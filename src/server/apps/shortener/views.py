from .models import URL
from rest_framework import generics
from .serializers import UrlSerializer
from ..utils.slug_generator import generate_slug
from django.views.generic import RedirectView
from rest_framework.generics import get_object_or_404


# Create your views here.


class UrlView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        serializer.save(slug=generate_slug())


class UrlRedirectView(RedirectView):
    permanent = True

    def get_redirect_url(self, slug):
        url = get_object_or_404(URL, slug=slug)
        url.increase_visits()
        return url.address
