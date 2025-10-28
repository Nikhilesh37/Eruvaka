from django.db import models
from .forms import ContactForm

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    your_email = models.EmailField()
    your_phone = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject
