from django.shortcuts import render
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.order_by('-timestamp')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/all_blog.html', context)