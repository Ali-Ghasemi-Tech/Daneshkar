from django.db import models
from membership.models import MemberModel
from django.utils import timezone
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

#adding this for effecincy

# class Contributor(models.Model):
#     ROLES = [
#         ('manager', 'Manager'),
#         ('leader', 'Leader'),
#         ('editor', 'Editor'),
#         ('viewer', 'Viewer'),
#     ]
#     user = models.ForeignKey(MemberModel , on_delete=models.CASCADE)
#     role = models.CharField(max_length=20 , choices=ROLES , default='viewer')


# class Workspace(models.Model):
#     title = models.CharField(max_length= 200)
#     private= models.BooleanField(default=True)
#     isActive = models.BooleanField(default=True)
#     contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)


# class Board(models.Model):
#     project_name = models.CharField(max_length=200)
#     description = models.TextField()
#     contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)
#     Workspace = models.ForeignKey(Workspace , on_delete=models.CASCADE)
#     is_active = models.BooleanField(default=True)
#     done = models.BooleanField(default=False)
#     due_date = models.DateTimeField(blank=True , null=True)
#     creation_date = models.DateTimeField(default=timezone.now())



# class Task(models.Model):
#     STATUS_CHOICES = [
#         ('todo', 'To Do'),
#         ('doing', 'Doing'),
#         ('suspend', 'Suspend'),
#         ('done', 'Done'),
#     ]
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo') 
#     board = models.ForeignKey(Board , on_delete=models.CASCADE)
#     contributors = models.ForeignKey(Contributor , on_delete=models.CASCADE)

class Workspace(models.Model):
    name = models.CharField(max_length=50 , null=True)
    owner = models.ForeignKey(MemberModel, on_delete=models.CASCADE, related_name='own_Workspace')
    members = models.ManyToManyField(MemberModel, related_name='Workspaces')
    is_active = models.BooleanField(default=True)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Workspace'
        verbose_name_plural = 'Workspaces'
        ordering = ['name']


class Board(models.Model):
    name = models.CharField(max_length=50 , null=True)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    done = models.BooleanField(default=False)
    start = models.DateTimeField(default=timezone.now)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='boards' , null=True)
    users = models.ManyToManyField(MemberModel, related_name='boards')

    # def clean(self):
    #     try:
    #         for user in self.users.all():
    #             if not self.Workspace.users.filter(id=user.id).exists():
    #                 raise ValidationError(f"the user {user} not in your Workspace")
    #     except ValueError:
    #         return False
        
    # def save(self, *args, **kwargs):
    #     if  self.clean():
    #         super().save(*args, **kwargs)
       

    class Meta:
        verbose_name = 'Board'
        verbose_name_plural = 'Boards'
        ordering = ['start']


class Task(models.Model):
    DO_CHOICES = [
        ('todo', 'todo'),
        ('doing', 'doing'),
        ('suspend', 'suspend'),
        ('done', 'done')
    ]
    TAGS = [
        ('new feature' , 'New Feature'),
        ('refactoring' , 'Refactoring'),
        ('bug fix' , 'Bug Fix'),
        ('r&d' , 'R&D')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField(default=timezone.now)
    deadline = models.DateTimeField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
    assigned_to = models.ForeignKey(MemberModel, on_delete=models.SET_NULL,
                                    related_name='assigned_tasks', null=True, blank=True)
    status = models.CharField(max_length=10, choices=DO_CHOICES, default='todo')
    tag =models.CharField(max_length=20 , choices=TAGS , null= True , blank= True)

    # def clean(self):
    #     if self.assigned_to and not self.board.users.filter(id=self.assigned_to.id).exists():
    #         raise ValidationError("the user isn't in your board")
    #     if self.end_time and self.end_time < self.start_time:
    #         raise ValidationError("the time has not passed the task")

    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)

    # def __str__(self):
    #     return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        ordering = ['title']
    