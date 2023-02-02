from django.urls import path
from . import views

urlpatterns = [
    path('authorization/', views.Authorization.as_view()),
    path('registration/', views.Registration.as_view()),
]
