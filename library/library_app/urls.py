from django.urls import path
from .views import custom_main


urlpatterns = [
    path('homepage/', custom_main, name='homepage'),
]