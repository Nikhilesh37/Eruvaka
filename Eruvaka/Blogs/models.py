from django.db import models

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
