from django.shortcuts import render , get_object_or_404 , redirect
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

    def get_context_data(self, **kwargs):
        context = super(PostDetailsView , self).get_context_data()
        user_post = get_object_or_404(Post , pk = self.kwargs['pk'])
        liked = False
        if user_post.like.filter(id = self.request.user.id).exists():
            liked = True
        context['liked'] = liked
        context['total_likes'] = user_post.total_likes()
        return context


class PostEditView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    fields = ['title' , 'text'] 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def like_view(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
    else:
        post.like.add(request.user)
    
    return redirect('post_detail' , pk = pk)

