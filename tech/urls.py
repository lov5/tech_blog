from django.contrib import admin
from django.urls import path,include
from tech import views


urlpatterns = [
    path('', views.index,name='tech'),
    path('about',views.about,name='about'),
    path('services',views.services,name='about'),
    path('contact',views.contact,name='contact'),
    path('councling',views.councling,name='councling'),



]
