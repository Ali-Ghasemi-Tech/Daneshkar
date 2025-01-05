from django.db import models
from accounts.models import CustomeUserModel

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length= 600)
    author = models.ForeignKey(CustomeUserModel , on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(CustomeUserModel , related_name='likes')

    def total_likes(self):
        return self.like.count()