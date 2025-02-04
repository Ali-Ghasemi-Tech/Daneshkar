from django.urls import path , include
from .views import SignUpView 
from .API.api import SignupApiView , DetailDeleteUpdateApiView , MemberListApiView 
urlpatterns =[
    path('' , include('django.contrib.auth.urls')),
    path('api/' , include('rest_framework.urls')),
    path('signup' , SignUpView.as_view() , name='signup'),
    path('api/signup/' , SignupApiView.as_view() , name='signup_api'),
    path('api/memberslist/' , MemberListApiView.as_view() , name = 'member_list'),
    path('api/<int:pk>/' , DetailDeleteUpdateApiView.as_view() , name= 'update_api'),
   
]