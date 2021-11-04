from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30)
    pwd_hash = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)

    def __str__(self):
        return f'<User {self.username} - {self.email}>'


class Dashboard(models.Model):
    title = models.CharField(max_length=50)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Dashboard {self.title} of User {self.user_id}>'


class PluginType(models.Model):
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    type_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.type_name} plugin {self.width}x{self.height}'


class Plugin(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    position = models.PositiveIntegerField()
    dashboard_id = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    type_id = models.ForeignKey(PluginType)

    class Meta:
        abstract = True

# Plugins
class NotesPlugin(Plugin):
    def __str__(self):
        return f'<Notes Plugin "{self.title}" - Position {self.position}>'


class NotesData(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    plugin_id = models.ForeignKey(NotesPlugin, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Note {self.title} - Plugin {self.plugin_id}>'


class TasksPlugin(Plugin):
    def __str__(self):
        return f'<Tasks Plugin "{self.title}" - Position {self.position}>'


class TasksData(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    due_date = models.DateTimeField()
    priority = models.IntegerField()
    plugin_id = models.ForeignKey(NotesPlugin, on_delete=models.CASCADE)

    def __str__(self):
        return f'<Task {self.title} due {self.due_date} - Plugin {self.plugin_id}>'