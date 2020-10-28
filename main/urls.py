from django.urls import path
from django.views.generic import TemplateView
from .views import ContactUsView

urlpatterns = [    
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('contact/', ContactUsView.as_view(template_name="contact.html"), name='contact'),
]
