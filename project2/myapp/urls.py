# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.card, name='card'),  # or whatever view you want to use
]
