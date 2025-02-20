from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'campaign/dashboard.html')
def campaigner (request):
    return render(request, 'campaign/campaigner.html')
def funder(request):
    return render(request, 'campaign/funder.html')