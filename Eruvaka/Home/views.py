from django.views.generic import ListView
from .models import category, items

class homeview(ListView):
    model = category
    template_name = 'home.html'
    context_object_name = 'cat'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best'] = items.objects.filter(tag__name='Best Sellers')
        context['new'] = items.objects.filter(tag__name='New Arrivals')
        context['feat'] = items.objects.filter(tag__name='Featured')
        return context

class productview(ListView):
    model = items
    template_name = 'product.html'
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = category.objects.all()
        context['best'] = items.objects.filter(tag__name='Best Sellers')
        context['feat'] = items.objects.filter(tag__name='Featured')
        return context
    