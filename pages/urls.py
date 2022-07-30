
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about_us'),
    path('contactus/', views.contactus, name='contactus'),
]
