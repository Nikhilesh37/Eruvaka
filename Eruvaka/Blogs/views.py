from .models import blogs
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    model = blogs
    template_name = "blogs.html"
    context_object_name = "blogs"
    paginate_by = 6

class BlogDetailView(DetailView):
    model = blogs
    template_name = "blog_detail.html"
    context_object_name = "blog"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'