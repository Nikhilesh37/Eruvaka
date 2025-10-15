from django.contrib import admin
from .models import *
# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(category)
admin.site.register(tag)
admin.site.register(items, ItemAdmin)
