from django.shortcuts import render
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/all_blog.html', context)