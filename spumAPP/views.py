from django.http import HttpResponse

def index(request):
    return HttpResponse("index.html, home.html")


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