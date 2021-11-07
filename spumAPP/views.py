from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from .forms import NewUserForm
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


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("templates:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
