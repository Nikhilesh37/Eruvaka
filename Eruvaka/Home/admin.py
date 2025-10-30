from django.contrib import admin
from .models import *
from django import forms
import json

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'static_image']
    search_fields = ['name']

@admin.register(items)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'old_price', 'ratings', 'Best_Sellers', 'New_Arrivals', 'Featured_Products']
    list_filter = ['category', 'Best_Sellers', 'New_Arrivals', 'Featured_Products']
    search_fields = ['name', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'static_image', 'ratings')
        }),
        ('Pricing', {
            'fields': ('price', 'old_price'),
            'description': 'Set product price'
        }),
        ('Categories & Features', {
            'fields': ('Best_Sellers', 'New_Arrivals', 'Featured_Products')
        }),
    )

