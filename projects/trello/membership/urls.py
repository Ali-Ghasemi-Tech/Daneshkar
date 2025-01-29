from django.urls import path , include
from .views import SignUpView , loginView
from .API.api import SignupApiView , UpdateApiView
urlpatterns =[
    path('signup' , SignUpView.as_view() , name='signup'),
    path('login/' , loginView , name='login'),
    path('api/signup/' , SignupApiView.as_view() , name='signup_api'),
    path('api/<int:pk>/update/' , UpdateApiView.as_view() , name= 'update_api'),
]