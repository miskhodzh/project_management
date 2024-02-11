from django.forms import ModelForm, DateInput

from . models import Project, Task

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
            'date_created',
        )


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'status',
            'priority',
            'due_date',
        )
        widgets = {
            'due_date': DateInput(attrs={'type': 'date'})
        }
