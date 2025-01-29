from django.db import models
from membership.models import MemberModel
from django.utils import timezone

# Create your models here.

#adding this for effecincy

class Contributor(models.Model):
    ROLES = [
        ('manager', 'Manager'),
        ('leader', 'Leader'),
        ('editor', 'Editor'),
        ('viewer', 'Viewer'),
    ]
    user = models.ForeignKey(MemberModel , on_delete=models.CASCADE)
    role = models.CharField(max_length=20 , choices=ROLES , default='viewer')


class Workspace(models.Model):
    title = models.CharField(max_length= 200)
    private= models.BooleanField(default=True)
    isActive = models.BooleanField(default=True)
    contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)


class Board(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace , on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    due_date = models.DateTimeField(default=timezone.now())

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('doing', 'Doing'),
        ('suspend', 'Suspend'),
        ('done', 'Done'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo') 
    board = models.ForeignKey(Board , on_delete=models.CASCADE)
    contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)
    