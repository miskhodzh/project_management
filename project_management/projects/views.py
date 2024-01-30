from django.shortcuts import render, get_object_or_404

from . forms import ProjectForm
from . models import Project, Task

def projects_add(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            project = Project(
                name=name,
                description=description
            )
            project.save()
    else:
        form = ProjectForm()
    
    projects = Project.objects.all()
    context = {
        'form': form,
        'projects': projects,
    }
    template = 'projects/add.html'
    return render(request, template, context)

def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
    }
    template = 'projects/list.html'
    return render(request, template, context)

def project(request, project_name):
    # task = get_object_or_404(Task)
    ...
