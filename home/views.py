from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'index.html', context)

def login(request):
    return render(request, 'login.html')
