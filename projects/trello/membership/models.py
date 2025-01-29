from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class MemberModel(models.Model):
    
    username = models.CharField(max_length=200 , unique=True)
    firstname= models.CharField(max_length=200 , blank=True , null = True)
    lastname= models.CharField(max_length=200 , blank=True , null = True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(blank=True ,null=True , unique=True)
    password= models.CharField(max_length=128)
    last_login = models.DateTimeField(null=True , blank= True)

    def save(self, *args , **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super().save(*args , **kwargs)
        




