from django.urls import path 
from .views import NewPost , PostDetailsView ,PostEditView , PostDeleteView , like_view ,dislike_view, CommentCreateView , CommentReplyView , DeleteCommentView

urlpatterns =[
    path('create_post' , NewPost.as_view() , name='new_post'),
    path('<int:pk>', PostDetailsView.as_view() , name='post_detail'),
    path('<int:pk>/update_post', PostEditView.as_view() , name='update_post'),
    path('<int:pk>/delete' , PostDeleteView.as_view() , name= 'delete_post'),
    path('<int:pk>/like_post' , like_view , name='like_post'),
    path('<int:pk>/dislike_post' ,dislike_view , name='dislike_post'),
    path('<int:post_pk>/post_comment' , CommentCreateView.as_view() , name='post_comment'),
    path('<int:post_pk>/post_comment/<int:comment_pk>/comment_reply' , CommentReplyView.as_view() , name='comment_reply'),
   path('<int:post_pk>/post_comment/<int:comment_pk>/delete' , DeleteCommentView.as_view() , name='delete_comment')
]