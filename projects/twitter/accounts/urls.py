from django.urls import path , include
from .views import SignUpView , MyProfileView , ProfileView , ProfilePostsView

urlpatterns=[
    path('profile' , MyProfileView.as_view() , name='my_profile'),
    path('profile/<str:username>/', ProfileView , name='view_profile'),
    path('signup' , SignUpView.as_view() , name='signup'),
    path('' , include('django.contrib.auth.urls'))
] 