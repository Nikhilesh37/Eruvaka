from django.contrib import admin
from .models import ProductWeight

class ProductWeightInline(admin.TabularInline):
    model = ProductWeight
    extra = 1
    fields = ('weight', 'weight_in_grams', 'price', 'old_price', 'is_default', 'in_stock')
    
@admin.register(ProductWeight)
class ProductWeightAdmin(admin.ModelAdmin):
    list_display = ('product', 'weight', 'price', 'old_price', 'discount_percentage', 'is_default', 'in_stock')
    list_filter = ('is_default', 'in_stock', 'product__category')
    search_fields = ('product__name', 'weight')
    list_editable = ('price', 'old_price', 'is_default', 'in_stock')
    ordering = ('product', 'weight_in_grams')

