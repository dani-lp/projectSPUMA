from django.contrib.auth.decorators import login_required
from django.urls import path
from spumAPP.views import *
from . import views


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('home/<int:dashboard_id>', login_required(HomeView.as_view()), name='home'),
    path('dashboard_delete', DashboardDeleteView.as_view(), name='dashboard_delete'),
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', login_required(LogoutView.as_view()), name='logout'),
    path('settings', login_required(SettingsView.as_view()), name='settings'),
    path('plugins/notes/<int:plugin_id>', login_required(NotesPluginsView.as_view()), name='notes_plugins'),
    path('plugins/tasks/<int:plugin_id>', login_required(TasksPluginsView.as_view()), name='tasks_plugins'),
    path('plugins/tasks/create', login_required(CreateTaskView.as_view()), name='create_task'),
    path('plugins/tasks/update', login_required(UpdateTaskView.as_view()), name='update_task'),
    path('plugins/tasks/delete', login_required(DeleteTaskView.as_view()), name='delete_task'),
    path('plugins/notes/create', login_required(CreateNoteView.as_view()), name='create_note'),
    path('plugins/notes/update', login_required(UpdateNoteView.as_view()), name='update_note'),
    path('plugins/notes/delete', login_required(DeleteNoteView.as_view()), name='delete_note'),
]

handler404 = 'spumAPP.views.error_handler_404'