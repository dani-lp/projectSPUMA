from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = { 'loggedIn': False }
    return render(request, "index.html", context)


def login(request):
    return HttpResponse("login.html")


def register(request):
    return HttpResponse("register.html")


def settings(request):
    return HttpResponse("settings.html")


def notes_plugins(request, plugin_id):
    return HttpResponse("notes.html")


def tasks_plugins(request, plugin_id):
    return HttpResponse("tasks.html")