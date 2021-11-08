# Generated by Django 3.2.9 on 2021-11-08 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spumAPP', '0002_auto_20211108_0926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasksdata',
            name='content',
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='plugin_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spumAPP.tasksplugin'),
        ),
        migrations.AlterField(
            model_name='tasksdata',
            name='priority',
            field=models.CharField(max_length=6),
        ),
    ]