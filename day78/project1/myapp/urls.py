from django.urls import path
from . import views
urlpatterns = [
    path('contact/manual/',views.contact_manual, name= 'contact_manual'),
    path('contact/model/',views.contact_modelform, name= 'contact_modelform'),
]