from django.urls import path
from . import views

urlpatterns = [
    path("", views.homeview, name="home"),
    path("aboutus/", views.aboutusview, name="aboutus"),
    path("blogs/", views.blogsview, name="blogs"),
    path("contactus/", views.contactusview, name="contactus"),
    path("products/", views.productsview, name="products"),
]
