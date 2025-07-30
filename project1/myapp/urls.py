from django.urls import path 
from . import views 
urlpatterns = [ 
    path('', views.home, name = 'home'), 
    path('about/',views.about, name = 'about'),
    path('projects/', views.projects_list, name='projects_list'),
     path('projects/tag/<str:tag>/', views.projects_list, name='projects_by_tag'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('contact/', views.contact, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),


] 