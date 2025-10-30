from django.contrib import admin
from .models import *
from django import forms
import json

@admin.register(category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'static_image']
    search_fields = ['name']

class ItemAdminForm(forms.ModelForm):
    weight_250g_price = forms.IntegerField(required=False, label='250g Price')
    weight_250g_old_price = forms.IntegerField(required=False, label='250g Old Price')
    
    weight_500g_price = forms.IntegerField(required=False, label='500g Price')
    weight_500g_old_price = forms.IntegerField(required=False, label='500g Old Price')
    
    weight_1kg_price = forms.IntegerField(required=False, label='1kg Price')
    weight_1kg_old_price = forms.IntegerField(required=False, label='1kg Old Price')
    
    weight_2kg_price = forms.IntegerField(required=False, label='2kg Price')
    weight_2kg_old_price = forms.IntegerField(required=False, label='2kg Old Price')
    
    weight_5kg_price = forms.IntegerField(required=False, label='5kg Price')
    weight_5kg_old_price = forms.IntegerField(required=False, label='5kg Old Price')
    
    class Meta:
        model = items
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.weight_prices:
            weight_data = self.instance.weight_prices
            if '250g' in weight_data:
                self.fields['weight_250g_price'].initial = weight_data['250g'].get('price')
                self.fields['weight_250g_old_price'].initial = weight_data['250g'].get('old_price')
            if '500g' in weight_data:
                self.fields['weight_500g_price'].initial = weight_data['500g'].get('price')
                self.fields['weight_500g_old_price'].initial = weight_data['500g'].get('old_price')
            if '1kg' in weight_data:
                self.fields['weight_1kg_price'].initial = weight_data['1kg'].get('price')
                self.fields['weight_1kg_old_price'].initial = weight_data['1kg'].get('old_price')
            if '2kg' in weight_data:
                self.fields['weight_2kg_price'].initial = weight_data['2kg'].get('price')
                self.fields['weight_2kg_old_price'].initial = weight_data['2kg'].get('old_price')
            if '5kg' in weight_data:
                self.fields['weight_5kg_price'].initial = weight_data['5kg'].get('price')
                self.fields['weight_5kg_old_price'].initial = weight_data['5kg'].get('old_price')
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        weight_prices = {}
        
        weights = [
            ('250g', 'weight_250g_price', 'weight_250g_old_price'),
            ('500g', 'weight_500g_price', 'weight_500g_old_price'),
            ('1kg', 'weight_1kg_price', 'weight_1kg_old_price'),
            ('2kg', 'weight_2kg_price', 'weight_2kg_old_price'),
            ('5kg', 'weight_5kg_price', 'weight_5kg_old_price'),
        ]
        
        for weight, price_field, old_price_field in weights:
            price = self.cleaned_data.get(price_field)
            old_price = self.cleaned_data.get(old_price_field)
            
            if price:
                weight_prices[weight] = {
                    'price': price,
                    'old_price': old_price if old_price else 0
                }
        
        instance.weight_prices = weight_prices
        
        if commit:
            instance.save()
        return instance

@admin.register(items)
class ItemAdmin(admin.ModelAdmin):
    form = ItemAdminForm
    list_display = ['name', 'category', 'price', 'old_price', 'ratings', 'Best_Sellers', 'New_Arrivals', 'Featured_Products']
    list_filter = ['category', 'Best_Sellers', 'New_Arrivals', 'Featured_Products']
    search_fields = ['name', 'category__name']
    prepopulated_fields = {'slug': ('name',)}
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'static_image', 'ratings')
        }),
        ('Default Pricing', {
            'fields': ('price', 'old_price', 'default_weight'),
            'description': 'Set default price and weight option'
        }),
        ('Weight-Based Pricing', {
            'fields': (
                ('weight_250g_price', 'weight_250g_old_price'),
                ('weight_500g_price', 'weight_500g_old_price'),
                ('weight_1kg_price', 'weight_1kg_old_price'),
                ('weight_2kg_price', 'weight_2kg_old_price'),
                ('weight_5kg_price', 'weight_5kg_old_price'),
            ),
            'description': 'Set different prices for different weight options. Leave blank if not applicable.'
        }),
        ('Categories & Features', {
            'fields': ('Best_Sellers', 'New_Arrivals', 'Featured_Products')
        }),
    )
