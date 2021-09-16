from .models import URL
from rest_framework import generics
from .serializers import UrlSerializer
from ..utils.slug_generator import generate_slug


# Create your views here.


class UrlView(generics.ListCreateAPIView):
    queryset = URL.objects.all()
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        serializer.save(slug=generate_slug())
