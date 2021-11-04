from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('plugins/notes/<int:plugin_id>', views.notes_plugins, name='notes_plugins'),
    path('plugins/tasks/<int:plugin_id>', views.tasks_plugins, name='tasks_plugins'),
]