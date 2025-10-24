# Eruvaka/ContactUs/views.py

from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages # Import messages framework

class ContactView(TemplateView):
    template_name = "contactus.html"

    def post(self, request, *args, **kwargs):
        # Retrieve form data from POST request
        first_name = request.POST.get('first-name', '')
        user_email = request.POST.get('your-email', '')
        phone = request.POST.get('your-phone', '')
        subject = request.POST.get('subject', '')
        message_body = request.POST.get('message', '')

        # --- Basic Validation (Optional but Recommended) ---
        if not all([first_name, user_email, subject, message_body]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, self.template_name)
        # Add more specific validation if needed (e.g., email format)

        # --- Construct Email ---
        email_subject = f"Contact Form Submission: {subject}"
        email_message = f"""
        You have received a new message from the Eruvaka contact form:

        Name: {first_name}
        Email: {user_email}
        Phone: {phone if phone else 'Not provided'}
        Subject: {subject}

        Message:
        {message_body}
        """
        sender_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.ADMIN_EMAIL] # Send to your inbox defined in settings

        # --- Send Email ---
        try:
            send_mail(
                email_subject,
                email_message,
                sender_email,
                recipient_list,
                fail_silently=False, # Set to True in production if you don't want errors to stop the request
            )
            # Add a success message
            messages.success(request, 'Thank you for your message! We will get back to you soon.')
            # Redirect to the same page (or a thank you page) after successful submission
            return redirect('contact')
        except Exception as e:
            # Handle potential email sending errors (log the error, show user message)
            messages.error(request, f'Sorry, there was an error sending your message: {e}. Please try again later.')
            # Optionally log the error `e` for debugging
            return render(request, self.template_name) # Render the form again with error

    # The get method remains the same to display the form initially
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)