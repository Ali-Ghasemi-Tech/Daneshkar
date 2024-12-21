from django.urls import path , include
from .views import SignUpView , ProfileView

urlpatterns=[
    path('profile' , ProfileView.as_view() , name='profile'),
    path('signup' , SignUpView.as_view() , name='signup'),
    path('' , include('django.contrib.auth.urls'))
]