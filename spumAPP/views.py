from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse, response
from .forms import CreateDashboardForm, CreateTaskForm, EditDashboardForm, RegisterForm, LoginForm, CreateNotesForm, EditNotesForm
from .models import *
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    loggedIn = not request.user.is_anonymous
    
    if loggedIn:
        user_dashboards = get_list_or_404(Dashboard.objects.filter(user_id=request.user).order_by("pk"));
        return redirect('home', dashboard_id=user_dashboards[0].id)
    else:
        context = {
            'loggedIn': loggedIn,
            'user': request.user,
            'isLanding': True,
        }
        return render(request, "index.html", context)
    

@login_required
def home(request, dashboard_id):
    loggedIn = not request.user.is_anonymous
    
    create_form = CreateDashboardForm()
    edit_form = EditDashboardForm()
    
    user_dashboards = get_list_or_404(Dashboard.objects.filter(user_id=request.user).order_by("pk"));
    initial_dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    
    if request.method == "POST":
        if 'create_dashboard' in request.POST:
            create_form = CreateDashboardForm(request.POST)
            if create_form.is_valid():
                title = create_form.cleaned_data['title']
                new_dashboard = Dashboard(title=title, user_id=request.user)
                new_dashboard.save()
                
                return redirect('home', dashboard_id=new_dashboard.id)
                
        elif 'edit_dashboard' in request.POST:
            edit_form = EditDashboardForm(request.POST)
            if edit_form.is_valid():
                new_title = edit_form.cleaned_data['title']
                initial_dashboard.title = new_title
                initial_dashboard.save()
                
                return redirect('home', dashboard_id=initial_dashboard.id)
    else:
        create_form = CreateDashboardForm()
        edit_form = EditDashboardForm()
    
    context = {
        'loggedIn': loggedIn,
        'user': request.user,
        'dashboard_list': user_dashboards,
        'dashboard_list_lenght': len(user_dashboards),
        'dashboard': initial_dashboard,
        'create_form': create_form,
        'edit_form': edit_form,
    }
    return render(request, "dashboard.html", context)


@csrf_exempt
def dashboard_delete(request):
    dashboard_id = request.POST.get('dashboard_id')
    dashboard = get_object_or_404(Dashboard, pk=dashboard_id)
    dashboard.delete()
    
    return redirect('index')


def register(request):
    if not request.user.is_anonymous:
        user_dashboards = get_list_or_404(Dashboard.objects.filter(user_id=request.user).order_by("pk"));
        return redirect('home', dashboard_id=user_dashboards[0].id)
    
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
            
            base_dashboard = Dashboard(title='Home dashboard', user_id=user)
            base_dashboard.save()
            
            return redirect('index')
    else:
        register_form = RegisterForm()
    context = {
        'register_form': register_form,
        'user': request.user,
        'loggedIn': not request.user.is_anonymous,
    }
    return render(request, "register.html", context)


def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                print('InvalidUser')
    else:
        login_form = LoginForm()
    context = {
        'login_form' : login_form,
        'user': request.user,
        'loggedIn': not request.user.is_anonymous,
    }
    return render(request, "login.html", context)


@login_required
def logout(request):
    if request.user.is_authenticated:
        django_logout(request)
    return redirect('index')


@login_required
def settings(request):
    return HttpResponse("settings.html")


@login_required
def notes_plugins(request, plugin_id):
    loggedIn = request.user.is_authenticated
    if (not loggedIn):
        return redirect('login')
    notes_plugin = NotesPlugin.objects.get(pk=plugin_id)
    notes_list = NotesData.objects.filter(plugin_id=plugin_id).order_by('title')
    
    create_notes_form = CreateNotesForm()
    edit_notes_form = EditNotesForm()
    context = {
        'user': request.user,
        'loggedIn': loggedIn,
        'notes_plugin': notes_plugin,
        'notes_list': notes_list,
        'create_notes_form': create_notes_form,
        'edit_notes_form': edit_notes_form,
        'plugin_id': plugin_id,
    }
    return render(request, "notes.html", context)


@login_required
def tasks_plugins(request, plugin_id):
    loggedIn = request.user.is_authenticated
    if (not loggedIn):
        return redirect('login')
    task_plugin = get_object_or_404(TasksPlugin, pk=plugin_id)
    task_list = get_list_or_404(TasksData.objects.filter(plugin_id=plugin_id).order_by('title'))
    
    create_task_form = CreateTaskForm()
    
    context = {
        'user': request.user,
        'loggedIn': loggedIn,
        'task_plugin': task_plugin,
        'task_list': task_list,
        'create_task_form': create_task_form,
        'plugin_id': plugin_id,
    }
    return render(request, "tasks.html", context)


@csrf_exempt
def create_note(request):
    if request.method == 'POST':
        noteTitle = request.POST.get('noteTitle')
        noteContent = request.POST.get('noteContent')
        plugin_id = request.POST.get('pluginId')
        
        plugin_obj = NotesPlugin.objects.get(pk=plugin_id)
        new_note = NotesData(title=noteTitle, content=noteContent, plugin_id=plugin_obj)
        new_note.save()
        
        json_data = {'note_id': new_note.id}

        return HttpResponse(json.dumps(json_data))


@csrf_exempt
def update_note(request):
    if request.method == 'POST':
        noteTitle = request.POST.get('noteTitle')
        content = request.POST.get('noteContent')
        noteID = request.POST.get('noteID')
        note = NotesData.objects.get(pk=noteID)
        note.title = noteTitle
        note.content = content
        note.save()
        json_data = {'note_id': noteID}

        return HttpResponse(json.dumps(json_data))
    
    
@csrf_exempt
def delete_note(request):
    if request.method == 'POST':
        noteID = request.POST.get('noteID')
        
        note = NotesData.objects.get(pk=noteID)
        note.delete()

        return HttpResponse('success')


@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        taskTitle = request.POST.get('taskTitle')
        taskPriority = request.POST.get('taskPriority')
        plugin_id = request.POST.get('pluginId')
        
        plugin_obj = TasksPlugin.objects.get(pk=plugin_id)
        new_task = TasksData(title=taskTitle, priority=taskPriority, done=False, plugin_id=plugin_obj);
        new_task.save()
        
        json_data = {'task_id': new_task.id}

        return HttpResponse(json.dumps(json_data))


@csrf_exempt
def update_task(request):
    if request.method == 'POST':
        isDone = request.POST.get('isDone') == 'true'
        taskID = request.POST.get('taskID')
        
        task = TasksData.objects.get(pk=taskID)
        task.done = isDone
        task.save()

        return HttpResponse('success')
    
    
@csrf_exempt
def delete_task(request):
    if request.method == 'POST':
        taskID = request.POST.get('taskID')
        
        task = TasksData.objects.get(pk=taskID)
        task.delete()

        return HttpResponse('success')
    
    
def error_handler_404(request, exception):
    return render(request, '404.html', status=404)