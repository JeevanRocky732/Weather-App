from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home', views.home, name='home'),
    path('results', views.results, name='results'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
]