from .views import UrlRedirectView, UrlView
from django.urls import path

app_name = 'shortener'

urlpatterns = [
    path('urls/', UrlView.as_view(), name='urls'),
    path('<slug:slug>/', UrlRedirectView.as_view(), name='url-redirect')
]
