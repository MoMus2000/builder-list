import json
from django.shortcuts import render, redirect
from django.http import JsonResponse

from projects.models import Project, Checklist, Design, Basement, F1, F2, Roof

def render_list_projects(request):
    projects = Project.objects.all() #pyright: ignore
    context = {
        "Projects": projects
    }
    return render(request, 'list-projects.html', context)

def save_to_checklist(request, project_id, checklist_id):
    if request.method == "POST":
        checklist = Checklist.objects.filter( # pyright: ignore
            id = checklist_id,
            project = project_id
        ).first()

        data = json.loads(request.body)

        print(data["sectionName"], data["text"])

        if data["sectionName"] == "Design":
            design = checklist.design
            design.todo_list.append(data["text"])
            design.save()

        if data["sectionName"] == "Roof":
            roof = checklist.roof
            roof.todo_list.append(data["text"])
            roof.save()

        if data["sectionName"] == "Basement":
            basement = checklist.basement
            basement.todo_list.append(data["text"])
            basement.save()

        if data["sectionName"] == "1st Floor":
            f1 = checklist.f1
            f1.todo_list.append(data["text"])
            f1.save()

        if data["sectionName"] == "2nd Floor":
            f2 = checklist.f2
            f2.todo_list.append(data["text"])
            f2.save()

        return JsonResponse({})

def render_create_project(request, id=None):
    if request.method == "POST" and id is None:
        project_name = request.POST.get("name")
        description  = request.POST.get("description")
        proj = Project(name = project_name, description = description)
        proj.save()
        
        design = Design.objects.create()
        roof = Roof.objects.create()
        f1 = F1.objects.create()
        f2 = F2.objects.create()
        basement = Basement.objects.create()

        Checklist(
            name = project_name,
            project = proj,
            design = design,
            roof   = roof,
            f1     = f1,
            f2     = f2,
            basement = basement
        ).save()
    elif request.method == "POST" and id is not None:
        Project.objects.filter(id=id).delete() # pyright: ignore
        return redirect("/")

    return render(request, 'create-project.html')

def render_checklist(request, id):
    project = Project.objects.filter(id=id).first() # pyright: ignore
    checklist = Checklist.objects.filter( # pyright: ignore
        project = project
    ).first() 

    context = {
        "Project"    : project,
        "Checklist"  : checklist,
    }

    print(checklist)

    print(checklist.design.todo_list)

    return render(request, 'checklist.html', context)

