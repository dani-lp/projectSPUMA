from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/<int:dashboard_id>', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('plugins/notes/<int:plugin_id>', views.notes_plugins, name='notes_plugins'),
    path('plugins/tasks/<int:plugin_id>', views.tasks_plugins, name='tasks_plugins'),
    path('plugins/tasks/create', views.create_task, name='create_task'),
    path('plugins/tasks/update', views.update_task, name='update_task'),
    path('plugins/tasks/delete', views.delete_task, name='delete_task'),
    path('plugins/notes/create', views.create_note, name='create_note'),
    path('plugins/notes/update', views.update_note, name='update_note'),
    path('plugins/notes/delete', views.delete_note, name='delete_note'),
]

handler404 = 'spumAPP.views.error_handler_404'