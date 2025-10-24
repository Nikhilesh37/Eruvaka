from django.contrib import admin
from .models import author, blogs

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(author, AuthorAdmin)

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(blogs, BlogsAdmin)
