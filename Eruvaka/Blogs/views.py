from django.shortcuts import render, get_object_or_404
from .models import blogs
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = blogs
    template_name = "blogs.html"
    context_object_name = "blogs"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BlogDetailView(DetailView):
    model = blogs
    template_name = "blog_detail.html"
    context_object_name = "blog"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'