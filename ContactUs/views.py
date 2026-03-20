from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import ContactForm

class ContactView(View):
    template_name = "contactus.html"

    def get(self, request):
        form = ContactForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            your_email = form.cleaned_data['your_email']
            your_phone = form.cleaned_data.get('your_phone', 'Not provided')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            print("\n" + "="*60)
            print("NEW CONTACT FORM SUBMISSION")
            print("="*60)
            print(f"Name: {first_name}")
            print(f"Email: {your_email}")
            print(f"Phone: {your_phone}")
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            print("="*60 + "\n")
            
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors in the form.')
        
        return render(request, self.template_name, {'form': form})
