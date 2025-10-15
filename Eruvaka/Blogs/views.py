from django.shortcuts import render
from .models import blogs
from django.views.generic import ListView
# Create your views here.
class BlogListView(ListView):
    model = blogs
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
