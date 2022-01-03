from django.contrib import admin
from .models import Dashboard, TasksPlugin, TasksData, NotesPlugin, NotesData, HabitsPlugin, HabitsData

admin.site.register(Dashboard)
admin.site.register(TasksPlugin)
admin.site.register(TasksData)
admin.site.register(NotesPlugin)
admin.site.register(NotesData)
admin.site.register(HabitsPlugin)
admin.site.register(HabitsData)