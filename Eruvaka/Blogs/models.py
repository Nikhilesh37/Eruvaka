from django.db import models

class author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class blogs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    excerpt = models.TextField(max_length=500, blank=True, help_text="Short description for blog card")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.title
