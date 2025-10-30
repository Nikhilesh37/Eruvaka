from django.shortcuts import render, get_object_or_404
from Home.models import items, category
from .models import ProductWeight
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

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
    """
    Product detail view - all price calculations done server-side
    Weight variants are pre-processed in context for template rendering
    """
    model = items
    template_name = 'product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get related products from the same category
        context['related_products'] = items.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:4]
        
        # Get weight variants for this product from ProductWeight model
        weight_variants = ProductWeight.objects.filter(product=self.object)
        context['weight_variants'] = weight_variants
        
        # Get default weight or first available weight
        default_weight = weight_variants.filter(is_default=True).first()
        if not default_weight:
            default_weight = weight_variants.first()
        context['default_weight'] = default_weight
        
        # Add selected weight from query params if present
        selected_weight = self.request.GET.get('weight')
        if selected_weight:
            selected_variant = weight_variants.filter(weight=selected_weight).first()
            if selected_variant:
                context['selected_weight'] = selected_variant
        
        return context


@require_http_methods(["GET"])
def get_weight_price(request, product_id, weight):
    """
    Django-based endpoint to get price for specific weight
    This replaces JavaScript-based price updates with server-side logic
    """
    try:
        weight_variant = ProductWeight.objects.get(product_id=product_id, weight=weight)
        
        # Calculate savings if old price exists
        savings = 0
        if weight_variant.old_price and weight_variant.old_price > weight_variant.price:
            savings = float(weight_variant.old_price - weight_variant.price)
        
        return JsonResponse({
            'success': True,
            'price': float(weight_variant.price),
            'old_price': float(weight_variant.old_price) if weight_variant.old_price else None,
            'in_stock': weight_variant.in_stock,
            'discount_percentage': weight_variant.discount_percentage,
            'savings': savings,
            'weight': weight_variant.weight
        })
    except ProductWeight.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Weight variant not found'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': str(e)
        }, status=500)
    