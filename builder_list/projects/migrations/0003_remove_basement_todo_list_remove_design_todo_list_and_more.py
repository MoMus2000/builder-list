# Generated by Django 5.2.1 on 2025-05-20 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_comment_todo_alter_basement_todo_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basement',
            name='todo_list',
        ),
        migrations.RemoveField(
            model_name='design',
            name='todo_list',
        ),
        migrations.RemoveField(
            model_name='f1',
            name='todo_list',
        ),
        migrations.RemoveField(
            model_name='f2',
            name='todo_list',
        ),
        migrations.RemoveField(
            model_name='roof',
            name='todo_list',
        ),
        migrations.AddField(
            model_name='todo',
            name='basement',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.basement'),
        ),
        migrations.AddField(
            model_name='todo',
            name='design',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.design'),
        ),
        migrations.AddField(
            model_name='todo',
            name='f1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.f1'),
        ),
        migrations.AddField(
            model_name='todo',
            name='f2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.f2'),
        ),
        migrations.AddField(
            model_name='todo',
            name='roof',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.roof'),
        ),
    ]
