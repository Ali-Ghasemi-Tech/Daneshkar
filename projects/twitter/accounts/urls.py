from django.urls import path , include
from .views import SignUpView , MyProfileView , ProfileView  , follow_view

urlpatterns=[
    path('profile' , MyProfileView.as_view() , name='my_profile'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='view_profile'),
    path('signup' , SignUpView.as_view() , name='signup'),
    path('' , include('django.contrib.auth.urls')),
    path('profile/<int:pk>/follow_account' ,follow_view , name='follow' )
] 