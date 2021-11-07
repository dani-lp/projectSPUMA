from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    loggedIn = False
    isLanding = request.user.is_authenticated
    context = { 
        'loggedIn': loggedIn,
        'isLanding': isLanding,
    }
    return render(request, "index.html", context)

def register(request):
    register_form = RegisterForm()
    context = {'register_form': register_form}
    return render(request, "register.html", context)

def login(request):
    context = { 'loggedIn': False }
    return render(request, "login.html", context)


# @login_required
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('index')


def settings(request):
    return HttpResponse("settings.html")


def notes_plugins(request, plugin_id):
    return HttpResponse("notes.html")


def tasks_plugins(request, plugin_id):
    return HttpResponse("tasks.html")
