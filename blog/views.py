from django.shortcuts import render
from .models import Post


def index(request):
    blog = Post.objects.all()
    
    return render(request, 'blog.html', {
        'blog': blog, 
    })