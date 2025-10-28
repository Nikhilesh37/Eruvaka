from django import views
from django.views.generic import TemplateView
from .models import  category, items
from django.shortcuts import render

class homeview(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] = category.objects.all()[:5]
        context["best"] = items.objects.filter(Best_Sellers=True)[:8]
        context["feat"] = items.objects.filter(Featured_Products=True)[:8]
        
        # Get all categories for the filter tabs
        all_categories_list = list(category.objects.all())
        context["all_categories"] = all_categories_list
        
        # Create category navigation list (including 'all' at the beginning)
        category_names = ['all'] + [cat.name for cat in all_categories_list]
        category_filter = self.request.GET.get('category', 'all')
        context["selected_category"] = category_filter
        try:
            current_index = category_names.index(category_filter.lower())
        except ValueError:
            current_index = 0
        
        # Calculate previous and next category
        prev_index = (current_index - 1) % len(category_names)
        next_index = (current_index + 1) % len(category_names)
        
        context["prev_category"] = category_names[prev_index]
        context["next_category"] = category_names[next_index]
        
        # Filter new arrivals based on category
        if category_filter.lower() == 'all':
            context["new"] = items.objects.filter(New_Arrivals=True).order_by('-id')[:6]
        else:
            context["new"] = items.objects.filter(
                New_Arrivals=True, 
                category__name__iexact=category_filter
            ).order_by('-id')[:6]
        
        return context
