from django.db import models

# Schema is Ugly, create a new model called Todos
# On those todo's there can be an optional model called Comment

class Project(models.Model):
    name        = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    todo    = models.ForeignKey('Todo', on_delete=models.DO_NOTHING)

class Todo(models.Model):
    todo = models.CharField(max_length=200)

    design = models.ForeignKey('Design', null=True, blank=True, on_delete=models.CASCADE)

    roof = models.ForeignKey('Roof', null=True, blank=True, on_delete=models.CASCADE)

    basement = models.ForeignKey('Basement', null=True, blank=True, on_delete=models.CASCADE)

    f1 = models.ForeignKey('F1', null=True, blank=True, on_delete=models.CASCADE)
    f2 = models.ForeignKey('F2', null=True, blank=True, on_delete=models.CASCADE)

class Design(models.Model):
    pass

class Roof(models.Model):
    pass

class F1(models.Model):
    pass

class F2(models.Model):
    pass

class Basement(models.Model):
    pass

class Checklist(models.Model):
    name     = models.CharField(max_length=200)
    project  = models.ForeignKey(Project, on_delete=models.CASCADE)
    design   = models.ForeignKey(Design,  on_delete=models.CASCADE)
    roof     = models.ForeignKey(Roof,    on_delete=models.CASCADE)
    f1       = models.ForeignKey(F1,      on_delete=models.CASCADE)
    f2       = models.ForeignKey(F2,      on_delete=models.CASCADE)
    basement = models.ForeignKey(Basement, on_delete=models.CASCADE)

