from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TaskPerformers(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    performer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.task.name} - {self.performer.username}'
