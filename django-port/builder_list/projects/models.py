from django.db import models

class Project(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Checklist(models.Model):
    name    = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Design(models.Model):
    todo_list = models.JSONField()
    checklist = models.ForeignKey(Checklist, on_delete=models.DO_NOTHING)

class Roof(models.Model):
    todo_list = models.JSONField()
    checklist = models.ForeignKey(Checklist, on_delete=models.DO_NOTHING)

class F1(models.Model):
    todo_list = models.JSONField()
    checklist = models.ForeignKey(Checklist, on_delete=models.DO_NOTHING)

class F2(models.Model):
    todo_list = models.JSONField()
    checklist = models.ForeignKey(Checklist, on_delete=models.DO_NOTHING)

class Basement(models.Model):
    todo_list = models.JSONField()
    checklist = models.ForeignKey(Checklist, on_delete=models.DO_NOTHING)

