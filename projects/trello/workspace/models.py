from django.db import models
from membership.models import MemberModel

# Create your models here.

#adding this for effecincy
# class Contributor(models.Model):
#     members = models.ForeignKey(MemberModel , on_delete=models.CASCADE)

class Workspace(models.Model):
    title = models.CharField(max_length= 200)
    owner = models.ForeignKey( MemberModel , on_delete= models.CASCADE )
    private= models.BooleanField(default=True)
    isActive = models.BooleanField(default=True)


# class Board(models.Model):
#     project_name = models.CharField(max_length=200)
#     contributors = models.ManyToManyField(Contributor)
#     leader = models.ForeignKey(Contributor , on_delete=models.CASCADE)

# class Task(models.Model):
#     pass
    