from django.urls import path 
from .views import NewPost , PostDetailsView ,PostEditView , PostDeleteView , like_view , CommentCreateView

urlpatterns =[
    path('create_post' , NewPost.as_view() , name='new_post'),
    path('<int:pk>', PostDetailsView.as_view() , name='post_detail'),
    path('<int:pk>/update_post', PostEditView.as_view() , name='update_post'),
    path('<int:pk>/delete' , PostDeleteView.as_view() , name= 'delete_post'),
    path('<int:pk>/like_post' , like_view , name='like_post'),
    path('<int:pk>/post_comment' , CommentCreateView.as_view() , name='post_comment')
]