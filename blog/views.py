from django.shortcuts import render

def all_blog(request):
    return render(request, 'blog/all_blog.html')