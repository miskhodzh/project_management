from django.urls import path

from . views import projects_add, projects_list, project

app_name = 'projects'
urlpatterns = [
    path('add/', projects_add, name='projects_add'),
    path('list/', projects_list, name='projects_list'),
    path('<str:project_name>', project, name='project')
]