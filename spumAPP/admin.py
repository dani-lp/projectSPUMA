from django.contrib import admin
from .models import Dashboard, PluginType, TasksPlugin, TasksData

admin.site.register(Dashboard)
admin.site.register(PluginType)
admin.site.register(TasksPlugin)
admin.site.register(TasksData)