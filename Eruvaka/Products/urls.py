from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.product_list.as_view(), name='product-list'),
]