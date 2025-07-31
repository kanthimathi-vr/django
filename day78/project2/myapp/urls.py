from django.urls import path
from . import views

urlpatterns = [
    path('newsletter/manual/', views.newsletter_manual, name='newsletter_manual'),
    path('newsletter/model/', views.newsletter_model, name='newsletter_model'),
]
