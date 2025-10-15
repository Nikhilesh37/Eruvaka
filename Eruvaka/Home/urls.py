from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeview.as_view(), name='home'),
    path('product/', views.productview.as_view(), name='product')
]
