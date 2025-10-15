from django.shortcuts import render
from Home.models import items
from django.views.generic import ListView
# Create your views here.
class product_list(ListView):
    model = items
    template_name = 'product_list.html'
    context_object_name = 'items'
    ordering = ['-created_at']
    