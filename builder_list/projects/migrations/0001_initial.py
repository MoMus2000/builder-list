# Generated by Django 5.2.1 on 2025-05-20 03:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='F1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='F2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Roof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_list', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('basement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.basement')),
                ('design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.design')),
                ('f1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.f1')),
                ('f2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.f2')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('roof', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.roof')),
            ],
        ),
    ]
