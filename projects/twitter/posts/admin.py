from django.contrib import admin
from .models import Post , CommentModel

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title' , 'text' , 'date_post']
    filter_horizontal = ['like' , 'dislike'] 

@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'body']
    
