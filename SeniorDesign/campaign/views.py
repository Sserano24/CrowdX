from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'campaign/index.html')

def projects(request):
    return render(request, 'campaign/projects.html')

def create_project(request):
    return render(request, 'campaign/create_project.html')

def signup(request):
    return render(request, 'campaign/signup.html')

def login(request):
    return render(request, 'campaign/login.html')

def about(request):
    return render(request, 'campaign/about.html')

def contact(request):
    return render(request, 'campaign/contact.html')

def project_detail(request, id):
    return render(request, 'campaign/project_detail.html', {'id': id})