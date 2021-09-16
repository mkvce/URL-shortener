from .views import UrlView
from django.urls import path

app_name = 'shortener'

urlpatterns = [
    path('urls/', UrlView.as_view(), name='urls'),
]
