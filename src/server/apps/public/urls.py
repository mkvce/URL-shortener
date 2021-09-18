from django.urls import path
import views

app_name = 'public'

urlpatterns = [
    path('index/', views.index, name='index')
]
