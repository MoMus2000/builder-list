from django.db import models

# Schema is Ugly, create a new model called Todos
# On those todo's there can be an optional model called Comment

class Project(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Design(models.Model):
    todo_list = models.JSONField(default=list)

class Roof(models.Model):
    todo_list = models.JSONField(default=list)

class F1(models.Model):
    todo_list = models.JSONField(default=list)

class F2(models.Model):
    todo_list = models.JSONField(default=list)

class Basement(models.Model):
    todo_list = models.JSONField(default=list)

class Comment(models.Model):
    comment = models.Model(max_length=1000)

class Todo(models.Model):
    todo = models.CharField(max_length=200)
    comment = models.ForeignKey(Comment, null=True, blank=True)

class Checklist(models.Model):
    name     = models.CharField(max_length=200)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    design   = models.ForeignKey(Design,  on_delete=models.CASCADE)
    roof     = models.ForeignKey(Roof,    on_delete=models.CASCADE)
    f1       = models.ForeignKey(F1,      on_delete=models.CASCADE)
    f2       = models.ForeignKey(F2,      on_delete=models.CASCADE)
    basement = models.ForeignKey(Basement, on_delete=models.CASCADE)

