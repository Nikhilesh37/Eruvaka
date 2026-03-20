from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    your_email = forms.EmailField(required=True)
    your_phone = forms.CharField(max_length=15, required=False)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
