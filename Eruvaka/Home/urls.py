from django.urls import path
from . import views
from Products.views import ProductDetailView

urlpatterns = [
    path("", views.homeview.as_view(), name="home"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="home-product-detail"), 
    path('new/',views.newview.as_view()) 
]
