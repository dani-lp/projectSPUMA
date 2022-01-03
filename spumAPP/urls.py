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
    path('plugins/habits/<int:plugin_id>', login_required(HabitsPluginsView.as_view()), name='habits_plugins'),
    path('api/notes', login_required(NotesApiView.as_view()), name='notes_api'),
    path('api/tasks', login_required(TasksApiView.as_view()), name='tasks_api'),
    path('api/habits', login_required(HabitsApiView.as_view()), name='habits_api'),
]

handler404 = 'spumAPP.views.error_handler_404'