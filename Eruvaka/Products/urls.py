from django.urls import path
from .views import ProductListView, ProductDetailView, get_weight_price

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('get-weight-price/<int:product_id>/<str:weight>/', get_weight_price, name='get-weight-price'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]
