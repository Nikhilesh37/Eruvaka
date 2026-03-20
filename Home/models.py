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
    
    def __str__(self):
        return self.name
