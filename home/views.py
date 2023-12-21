from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}

    return render(request, 'index.html', context)

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, 'User does not exist')
        
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'login.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('home')
