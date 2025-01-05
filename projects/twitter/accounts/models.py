from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomeUserModel(AbstractUser):
    bio = models.TextField(max_length= 500 , null=True , blank=True)
    picture = models.FileField(blank=True)
    follow = models.ManyToManyField('self' , related_name='follows',symmetrical=False)

    def total_followers(self):
        return self.follow.count()
    
    # def user_posts(self) -> models.QuerySet:
    #     from posts.models import Post

    #     return Post.objects.filter(author = self)
