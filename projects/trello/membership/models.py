from django.db import models

# Create your models here.

class MemberModel(models.Model):
    username = models.CharField(max_length=200 , unique=True)
    firstname= models.CharField(max_length=200 , blank=True , null = True)
    lastname= models.CharField(max_length=200 , blank=True , null = True)
    isActive = models.BooleanField(default=True)
    email = models.EmailField(blank=True ,null=True , unique=True)
    password= models.CharField(max_length=200)


        




