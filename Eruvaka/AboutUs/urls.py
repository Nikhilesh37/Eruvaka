from django.urls import path
from . import views

urlpatterns = [
    path("", views.aboutview.as_view(), name="about"),
]