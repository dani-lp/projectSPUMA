from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('plugins/notes/<int:plugin_id>', views.notes_plugins, name='notes_plugins'),
    path('plugins/tasks/<int:plugin_id>', views.tasks_plugins, name='tasks_plugins'),
    path('plugins/tasks/update', views.tasks_update, name='updateTask'),
]