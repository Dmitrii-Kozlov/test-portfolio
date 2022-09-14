from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blog(request):
    blogs = Blog.objects.order_by('-timestamp')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/all_blog.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog': blog
    }
    return render(request, 'blog/detail.html', context)
