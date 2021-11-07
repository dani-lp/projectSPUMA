from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    loggedIn = request.user.is_anonymous
    isLanding = True
    print('LOGGED:' + request.user)
    context = {
        'loggedIn': loggedIn,
        'isLanding': isLanding,
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            email = register_form.cleaned_data['email']
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']

            User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user = authenticate(request, username=username, password=password)
            django_login(request, user)
            return redirect('index')
    else:
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
