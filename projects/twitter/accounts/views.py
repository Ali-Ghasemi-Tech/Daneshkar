from django.shortcuts import render
from django.views.generic import CreateView , UpdateView
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomeUserCreationForm
from django.urls import reverse_lazy
from .models import CustomeUserModel
from posts.models import Post
from django.views.generic import ListView
from django.shortcuts import render , get_object_or_404
# Create your views here.

class SignUpView(CreateView):
    form_class = CustomeUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class MyProfileView(UpdateView):
    model = CustomeUserModel
    template_name = 'profile.html'
    success_url = reverse_lazy('home')
    fields = ['username' , 'first_name' , 'last_name', 'email' , 'bio' , 'picture']


    def get_object(self): 
        return self.request.user 
    

class ProfilePostsView(ListView):
    template_name = 'view_profile.html'

    def get_queryset(self):
        profile = get_object_or_404(CustomeUserModel, username=self.kwargs.get('username')) 
        return Post.objects.filter(author=profile)


def ProfileView(request , username):
    profile = get_object_or_404(CustomeUserModel , username = username)
    posts = ProfilePostsView.as_view()(request , username = username) 
    return render(request , "view_profile.html" , {'profile' : profile , 'posts' : posts.get('object_list')})