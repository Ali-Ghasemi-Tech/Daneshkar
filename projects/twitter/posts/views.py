from django.shortcuts import render , get_object_or_404 , redirect
from django.views.generic import ListView , CreateView , DeleteView , UpdateView ,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post , CommentModel


# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name= 'home.html'
    context_object_name = 'posts'

class NewPost(CreateView , LoginRequiredMixin):
    model = Post
    template_name = 'post/new_post.html'
    context_object_name = 'posts'
    fields = ['title' , 'text']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailsView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetailsView , self).get_context_data()
        user_post = get_object_or_404(Post , pk = self.kwargs['pk'])
        liked = False
        disliked = False
        if user_post.like.filter(id = self.request.user.id).exists():
            liked = True
        elif user_post.dislike.filter(id = self.request.user.id).exists():
            disliked = True
        context['disliked'] = disliked
        context['liked'] = liked
        context['total_likes'] = user_post.total_likes()
        context['total_dislikes'] = user_post.total_dislikes()

       
        
        comments = user_post.comments.all().order_by('-created_at')
        context['comments'] = comments
        return context


class PostEditView(UpdateView):
    model = Post
    template_name = 'post/update_post.html'
    success_url = reverse_lazy('home')
    fields = ['title' , 'text'] 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/delete_post.html'
    success_url = reverse_lazy('home')


def like_view(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
    elif post.dislike.filter(id= request.user.id).exists():
        post.like.add(request.user)
        post.dislike.remove(request.user)
    else:
        post.like.add(request.user)
    
    return redirect('post_detail' , pk = pk)

def dislike_view(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if post.dislike.filter(id= request.user.id).exists():
        post.dislike.remove(request.user)
    elif post.like.filter(id= request.user.id).exists():
        post.like.remove(request.user)
        post.dislike.add(request.user)
    else:
        post.dislike.add(request.user)
    return redirect('post_detail', pk = pk)

class CommentCreateView(CreateView):
    model = CommentModel
    fields = ['body']
    template_name = 'post/comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_pk']

        form.instance.author = self.request.user
        
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail' , args=[self.object.post.pk])
    
    
    

class CommentReplyView(CreateView):
    model = CommentModel
    fields = ['body']    
    template_name = 'post/comment.html'

    def form_valid(self, form):
        post_pk = self.kwargs['post_pk']
        comment_pk = self.kwargs['comment_pk']
        parent_comment = CommentModel.objects.get(pk=comment_pk)

        form.instance.post_id = post_pk
        form.instance.author = self.request.user
        form.instance.reply = parent_comment  # Set the parent comment

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post_detail' , args=[self.object.post.pk])
    

   

class DeleteCommentView(DeleteView):
    model = CommentModel
    template_name = 'post/delete_comment.html'
    
    def get_object(self, **kwargs):
        pk = self.kwargs.get('comment_pk')  # Assuming you have 'pk' in your URL pattern
        return self.get_queryset().get(pk=pk)
    
    def get_success_url(self):
        return reverse_lazy('post_detail', args=[self.object.post.pk]) 

    