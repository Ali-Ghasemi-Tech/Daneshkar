from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MemberModel(AbstractUser):
    
    username = models.CharField(max_length=200 , unique=True)
    email = models.EmailField(blank=True ,null=True , unique=True )

    def __repr__(self):
        return self.username
    
    class Meta:
        app_label = 'membership'
   





