from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("index.html, home.html")


def login(request):
    return HttpResponse("login.html")


def register(request):
    context = {}
    return render(request, "register.html", context)


def settings(request):
    return HttpResponse("settings.html")


def notes_plugins(request, plugin_id):
    return HttpResponse("notes.html")


def tasks_plugins(request, plugin_id):
    return HttpResponse("tasks.html")