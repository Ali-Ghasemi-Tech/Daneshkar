from django.db import models
from accounts.models import CustomeUserModel
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length= 600)
    author = models.ForeignKey(CustomeUserModel , on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)
    like = models.ManyToManyField(CustomeUserModel , related_name='likes')

    def total_likes(self):
        return self.like.count()
    

class CommentModel(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE ,related_name='comments')
    reply = models.ForeignKey('self' , related_name='replies' , null=True , blank=True , on_delete=models.CASCADE)
    author = models.ForeignKey(CustomeUserModel , on_delete=models.CASCADE ,  related_name='comment_author')
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_abseloute_url(self):
        return reverse('post_detail' , args=str(self.post.id))