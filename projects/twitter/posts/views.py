from django.shortcuts import render
from django.views.generic import ListView , CreateView , DeleteView , UpdateView ,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


# Create your views here.
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name= 'home.html'
    context_object_name = 'posts'

class NewPost(CreateView , LoginRequiredMixin):
    model = Post
    template_name = 'new_post.html'
    context_object_name = 'posts'
    fields = ['title' , 'text']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailsView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostEditView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    fields = ['title' , 'text'] 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


    

