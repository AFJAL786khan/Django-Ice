from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.index, name="MyApp"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact;"),
    
]
