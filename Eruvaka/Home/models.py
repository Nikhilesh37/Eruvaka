from django.db import models
import json

class category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics', blank=True, null=True)
    static_image=models.CharField(max_length=200, blank=True, null=True)
    def __str__(self):
        return self.name

class items(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    static_image=models.CharField(max_length=200, blank=True, null=True)
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    old_price=models.IntegerField(default=0, null=True)
    slug = models.SlugField(max_length=200, null=True)
    ratings=models.FloatField(default=0, null=True)
    Best_Sellers=models.BooleanField(default=False)
    New_Arrivals=models.BooleanField(default=False)
    Featured_Products=models.BooleanField(default=False)
    weight_prices = models.JSONField(
        default=dict, 
        blank=True,
        help_text='{"250g": {"price": 100, "old_price": 120}, "500g": {"price": 200, "old_price": 240}}'
    )
    default_weight = models.CharField(max_length=20, default='500g', help_text='Default weight option')
    
    def __str__(self):
        return self.name
    
    def get_weight_options(self):
        """Return list of available weights"""
        if self.weight_prices:
            return list(self.weight_prices.keys())
        return []
    
    def get_price_for_weight(self, weight):
        """Get price for specific weight"""
        if self.weight_prices and weight in self.weight_prices:
            return self.weight_prices[weight].get('price', self.price)
        return self.price
    
    def get_old_price_for_weight(self, weight):
        """Get old price for specific weight"""
        if self.weight_prices and weight in self.weight_prices:
            return self.weight_prices[weight].get('old_price', self.old_price)
        return self.old_price
