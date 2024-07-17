from django.shortcuts import render

# Create your views here.



posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Testings',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
     {
        'author': 'Alex',
        'title': 'New Testings',
        'content': 'Second post content',
        'date_posted': 'September 27, 2018'
    }
]

def home(request):
    return render(request, 'home.html')

def post(request):
    contex = {'posts': posts}
    return render(request, 'blog/post.html', contex)