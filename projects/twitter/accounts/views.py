from django.views.generic import CreateView , UpdateView , DetailView
from django.contrib.auth.forms import UserCreationForm 
from .forms import CustomeUserCreationForm
from django.urls import reverse_lazy
from .models import CustomeUserModel
from posts.models import Post
from django.views.generic import ListView
from django.shortcuts import render , get_object_or_404 , redirect
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

    def get_context_data(self, **kwargs):
        context = super(MyProfileView , self).get_context_data()
       

        return context

    def get_object(self): 
        return self.request.user 
    

# class ProfilePostsView(ListView):
#     template_name = 'view_profile.html'

#     def get_queryset(self):
#         profile = get_object_or_404(CustomeUserModel, username=self.kwargs.get('username')) 
#         return Post.objects.filter(author=profile)


# def ProfileView(request , username):
#     profile = get_object_or_404(CustomeUserModel , username = username)
#     return render(request , "view_profile.html" , {'profile' : profile})

class ProfileView(DetailView):
    model = CustomeUserModel
    template_name = 'view_profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(ProfileView , self).get_context_data()

        user_post = get_object_or_404(CustomeUserModel , pk = self.kwargs['pk'])
        followed = False
        if user_post.follow.filter(id = self.request.user.id).exists():
            followed = True
        context['followed'] = followed
        context['total_followers'] = user_post.total_followers()

        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     user_post = get_object_or_404(CustomeUserModel , pk = self.kwargs['pk'])
    #     context['user_posts'] = user_post.user_posts() 
    #     return context


    

def follow_view(request , pk):
    user = get_object_or_404(CustomeUserModel , pk = pk)
    if user.follow.filter(id = request.user.id).exists():
        user.follow.remove(request.user)
    else:
        user.follow.add(request.user)
    return redirect('view_profile' , pk = pk)