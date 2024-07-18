from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.



# posts = [
#     {
#         'author': 'CoreyMS',
#         'title': 'Blog Testings',
#         'content': 'First post content',
#         'date_posted': 'August 27, 2018'
#     },
#      {
#         'author': 'Alex',
#         'title': 'New Testings',
#         'content': 'Second post content',
#         'date_posted': 'September 27, 2018'
#     }
# ]

def home(request):
    model = Post
    context = {'posts' : Post.objects.all()}
    return render(request, 'home.html', context)

def post(request):
    contex = 's'
    return render(request, 'blog/post.html', contex)

# class Post(ListView):
#     model = Post
#     context = Post.objects.all()
#     blog = 'home.html'