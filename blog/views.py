from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.




class PostListView(ListView):
    model = Post
    context = Post.objects.all().order_by('-date')
    template_name = 'home.html'
    paginate_by = 3
    
    
class PostListDetailsView(ListView):
    model = Post
    context = Post.objects.all().order_by('-date')
    template_name = 'blog/post.html'
    paginate_by = 10
    
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html' #Can be changed to post_detail.html
    