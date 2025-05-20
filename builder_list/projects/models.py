from django.db import models

class Project(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Design(models.Model):
    todo_list = models.JSONField(default=list) # make back into a dict, if a comment key
    # is set that means a comment has been written

class Roof(models.Model):
    todo_list = models.JSONField(default=list)

class F1(models.Model):
    todo_list = models.JSONField(default=list)

class F2(models.Model):
    todo_list = models.JSONField(default=list)

class Basement(models.Model):
    todo_list = models.JSONField(default=list)

class Checklist(models.Model):
    name     = models.CharField(max_length=200)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    design   = models.ForeignKey(Design,  on_delete=models.CASCADE)
    roof     = models.ForeignKey(Roof,    on_delete=models.CASCADE)
    f1       = models.ForeignKey(F1,      on_delete=models.CASCADE)
    f2       = models.ForeignKey(F2,      on_delete=models.CASCADE)
    basement = models.ForeignKey(Basement, on_delete=models.CASCADE)

