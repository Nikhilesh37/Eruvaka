from django.db import models
from Home.models import items

class ProductWeight(models.Model):
    product = models.ForeignKey(items, on_delete=models.CASCADE, related_name='weight_variants')
    weight = models.CharField(max_length=50, help_text="e.g., 500g, 1kg, 2kg, 5kg")
    weight_in_grams = models.IntegerField(help_text="Weight in grams for sorting")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_default = models.BooleanField(default=False, help_text="Default weight option for this product")
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['weight_in_grams']
        unique_together = ['product', 'weight']
        verbose_name = 'Product Weight Variant'
        verbose_name_plural = 'Product Weight Variants'
    
    def __str__(self):
        return f"{self.product.name} - {self.weight} - Rs.{self.price}"
    
    def save(self, *args, **kwargs):
        if self.is_default:
            ProductWeight.objects.filter(product=self.product, is_default=True).update(is_default=False)
        super().save(*args, **kwargs)
    
    @property
    def discount_percentage(self):
        if self.old_price and self.old_price > self.price:
            return int(((self.old_price - self.price) / self.old_price) * 100)
        return 0