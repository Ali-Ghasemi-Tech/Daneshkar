from django.shortcuts import render
from django.views.generic import CreateView , UpdateView
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ProfileView(UpdateView):
    model = User
    template_name = 'profile.html'
    success_url = reverse_lazy('profile')
    fields = ['username' , 'first_name' , 'last_name', 'email']


    def get_object(self): 
        return self.request.user 
   