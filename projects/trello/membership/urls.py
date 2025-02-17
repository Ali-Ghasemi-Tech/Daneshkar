from django.urls import path , include
from .views import SignupApiView , DetailDeleteUpdateApiView , MemberListApiView 
urlpatterns =[
    path('' , include('rest_framework.urls')),
    path('signup/' , SignupApiView.as_view() , name='signup_api'),
    path('memberslist/' , MemberListApiView.as_view() , name = 'member_list'),
    path('<int:pk>/' , DetailDeleteUpdateApiView.as_view() , name= 'update_api'),
   
]