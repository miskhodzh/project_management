from django.urls import path
from .views import ProjectAdd, ProjectEdit

app_name = 'project'
urlpatterns = [
    path('add/', ProjectAdd.as_view(), name='add_project'),
    path('edit/<int:pk>', ProjectEdit.as_view(), name='edit_project'),
]
