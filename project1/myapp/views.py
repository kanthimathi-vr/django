from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.mail import send_mail  
from django.contrib import messages 
# Create your views here.
def home(request):
    # return HttpResponse("Kanthimathi- portfolio")
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html') 
 
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # app directory
import os
import json

from django.http import Http404
from .projects_data import projects as projects_data, tag_list as tag_list_data

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

USE_JSON = False  # Set to True if you want to load from JSON file instead of Python data

def load_projects():
    if USE_JSON:
        with open(os.path.join(BASE_DIR, 'projects.json')) as f:
            projects = json.load(f)
        # Extract all unique tags from loaded JSON projects
        all_tags = sorted({tag for p in projects for tag in p['tags']})
        return projects, all_tags
    else:
        # Use imported Python data
        return projects_data, tag_list_data


def projects_list(request, tag=None):
    projects, all_tags = load_projects()

    if tag:
        projects = [p for p in projects if tag in p['tags']]

    context = {
        'projects': projects,
        'tag_list': all_tags,
        'tag': tag,
    }
    return render(request, 'myapp/projects.html', context)


def project_detail(request, slug):
    projects, _ = load_projects()

    project = next((p for p in projects if p['slug'] == slug), None)
    if not project:
        raise Http404("Project not found")

    return render(request, 'myapp/project_detail.html', {'project': project})

  
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Handle the form — e.g., save or send email
        print(f"Message from {name} ({email}): {message}")  # or send_email()

        return redirect('contact_success')  # make sure you have this URL pattern

    return render(request, 'myapp/contact.html')

def contact_success(request):
    return render(request, 'myapp/contact_success.html')
