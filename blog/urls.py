from django.urls import path
from .views import all_blog, detail

app_name = 'blog'

urlpatterns = [
    path('', all_blog, name='all_blog'),
    path('<int:blog_id>', detail, name='detail'),
]