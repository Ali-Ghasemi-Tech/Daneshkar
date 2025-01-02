from django.urls import path
from .views import NewPost

urlpatterns =[
    path('' , NewPost.as_view() , name='new_post')
]