from django.shortcuts import render, get_object_or_404
from Home.models import items, category
from django.views.generic import ListView, DetailView
from django.db.models import Q

class ProductListView(ListView):
    model = items
    template_name = 'products.html'
    context_object_name = 'items'
    paginate_by = 16
    
    def get_queryset(self):
        queryset = items.objects.all()
        
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        filter_type = self.request.GET.get('filter')
        if filter_type == 'bestseller':
            queryset = queryset.filter(Best_Sellers=True)
        elif filter_type == 'popular':
            queryset = queryset.filter(Featured_Products=True)
        elif filter_type == 'new':
            queryset = queryset.filter(New_Arrivals=True)
        
        return queryset.order_by('-id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = category.objects.all()
        context['current_category'] = self.request.GET.get('category', '')
        context['current_filter'] = self.request.GET.get('filter', '')
        context['search_query'] = self.request.GET.get('search', '')
        
        context['total_items'] = items.objects.count()
        context['bestseller_count'] = items.objects.filter(Best_Sellers=True).count()
        context['popular_count'] = items.objects.filter(Featured_Products=True).count()
        context['new_count'] = items.objects.filter(New_Arrivals=True).count()
        
        return context


class ProductDetailView(DetailView):
    model = items
    template_name = 'product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_products'] = items.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        return context
    