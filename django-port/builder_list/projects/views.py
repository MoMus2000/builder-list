from django.shortcuts import render, redirect

from projects.models import Project

def render_list_projects(request):
    projects = Project.objects.all() #pyright: ignore
    context = {
        "Projects": projects
    }
    return render(request, 'list-projects.html', context)

def render_create_project(request, id=None):
    if request.method == "POST" and id is None:
        project_name = request.POST.get("name")
        description  = request.POST.get("description")
        Project(name = project_name, description = description).save()
    elif request.method == "POST" and id is not None:
        Project.objects.filter(id=id).delete() # pyright: ignore
        return redirect("/")

    return render(request, 'create-project.html')

def render_checklist(request, id):
    project = Project.objects.filter(id=id).first() # pyright: ignore
    
    context = {
        "Project" : project
    }

    return render(request, 'checklist.html', context)

