from django.db import models

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='pics')
    def __str__(self):
        return self.name
class tag(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
class items(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    tag=models.ManyToManyField(tag)
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    old_price=models.IntegerField(default=0, null=True)
    slug = models.SlugField(max_length=200, null=True)
    ratings=models.FloatField(default=0, null=True)
    def __str__(self):
        return self.name
