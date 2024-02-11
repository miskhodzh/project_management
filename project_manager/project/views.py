from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect


from .froms import ProjectForm, TaskForm
from .models import Project, Task

class ProjectAdd(View):
    template = 'project/add.html'

    def get(self, request):
        form = ProjectForm()
        projects = Project.objects.all()
        context = {
            'form': form,
            'projects': projects,
        }
        return render(request, self.template, context)
    
    def post(self, request):
        print('Сработал метод который обрабатывает POST')
        form = ProjectForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            date_created = form.cleaned_data['date_created']
            owner = form.cleaned_data['owner']

            project = Project(
                title=title,
                description=description,
                date_created=date_created,
                owner=owner
            )
            project.save()
            return redirect('project:edit_project', pk=project.id)


class ProjectEdit(View):
    template = 'project/edit.html'

    def get(self, request, pk):
        form = TaskForm()
        project = Project.objects.get(pk=pk)
        tasks = Task.objects.filter(project=pk)
        context = {
            'project': project,
            'form': form,
            'tasks': tasks,
        }
        return render(request, self.template, context)

    def post(self, request, pk):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = Project.objects.get(pk=pk)
            task.save()
        return redirect('project:edit_project', pk=pk)
        