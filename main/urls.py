from django.urls import path
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .views import ContactUsView, ProductListView
from main import models

urlpatterns = [    
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', ContactUsView.as_view(template_name="contact.html"), name='contact'),
    path('products/<slug:tag>/', ProductListView.as_view(), name='products'),
    path('product/<slug:slug>/', DetailView.as_view(model=models.Product,  template_name = 'product_detail.html'), name='products'),
]
