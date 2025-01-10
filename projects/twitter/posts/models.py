from django.db import models
from accounts.models import CustomeUserModel
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

# Create your models here.


   
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length= 600)
    author = models.ForeignKey(CustomeUserModel , on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)
    time_post = models.TimeField(default=timezone.now() + timedelta(hours=3, minutes=30))
    image = models.ImageField(null=True , blank=True ,upload_to='post_pics/')
    tag = models.CharField(max_length=100 , null=True , blank=True)
    like = models.ManyToManyField(CustomeUserModel , related_name='likes' , null=True , blank=True)
    dislike = models.ManyToManyField(CustomeUserModel , related_name='dislikes' , null=True , blank=True)

    def total_likes(self):
        return self.like.count()
    
    def total_dislikes(self):
        return self.dislike.count()
    

class CommentModel(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE ,related_name='comments')
    reply = models.ForeignKey('self' , related_name='replies' , null=True , blank=True , on_delete=models.CASCADE)
    author = models.ForeignKey(CustomeUserModel , on_delete=models.CASCADE ,  related_name='comment_author')
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.PositiveIntegerField(default=1) 
    style = models.TextField(max_length=200 , blank=True , null=True)


    def get_abseloute_url(self):
        return reverse('post_detail' , args=str(self.post.id))
    
    def save(self, *args, **kwargs):
        if self.reply:
            self.level = self.reply.level + 1
            self.style = f"margin-left:calc({self.level} * 20) px"

        super(CommentModel, self).save(*args, **kwargs) 
    

    
