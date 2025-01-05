from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUserModel(AbstractUser):
    bio = models.TextField(max_length= 500 , null=True , blank=True)
    picture = models.FileField(blank=True)

