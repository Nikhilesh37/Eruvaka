from django.shortcuts import render
from .models import category, items, tag, Blog, Contact
from django.core.mail import send_mail
from django.conf import settings

def homeview(request):
	featured_tag = tag.objects.get(name='Featured')
	bestseller_tag = tag.objects.get(name='Bestseller')
	new_tag = tag.objects.get(name='New Arrival')
	return render(request, "home.html", {
		"cat": category.objects.all(),
		"best": items.objects.filter(tag=bestseller_tag)[:8],
		"new": items.objects.filter(tag=new_tag)[:3],
		"feat": items.objects.filter(tag=featured_tag)[:8],
	})

def aboutusview(request):
	return render(request, "aboutus.html")

def blogsview(request):
	blogs = Blog.objects.all().order_by('-date')
	return render(request, "blogs.html", {"blogs": blogs})

def contactusview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()

        # Send email
        subject = f'New message from {name}'
        message_body = f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['your-email@gmail.com']  # Replace with your email
        send_mail(subject, message_body, from_email, recipient_list)
        
        return render(request, "contactus.html", {'message_sent': True})
    return render(request, "contactus.html")

def productsview(request):
	all_items = items.objects.all()
	return render(request, "products.html", {
		"items": all_items,
		"item_count": all_items.count()
	})
