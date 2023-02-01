from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('authorization/', views.authorization),
    path('registration/', views.registration),
]
