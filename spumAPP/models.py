from django.db import models
from django.contrib.auth.models import User


class Plugin(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

# Plugins
class NotesPlugin(Plugin):
    def __str__(self):
        return f'<Notes Plugin "{self.title}"- ID: {self.id}>'


class TasksPlugin(Plugin):
    def __str__(self):
        return f'<Tasks Plugin "{self.title}" - ID: {self.id}">'


class NotesData(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    plugin_id = models.ForeignKey(NotesPlugin, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Note {self.title} - Plugin {self.plugin_id}>'


class TasksData(models.Model):
    title = models.CharField(max_length=50)
    priority = models.CharField(max_length=6)
    done = models.BooleanField(default=False)
    plugin_id = models.ForeignKey(TasksPlugin, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Task {self.title} Done{self.done} - Plugin {self.plugin_id}>'


class Dashboard(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_plugin = models.OneToOneField(NotesPlugin, on_delete=models.CASCADE, null=True)
    tasks_plugin = models.OneToOneField(TasksPlugin, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'<Dashboard {self.title} of User {self.user_id}>'
