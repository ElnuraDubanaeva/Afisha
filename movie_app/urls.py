
from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('movies/', views.movie_all_view),
    path('movies/<int:id_>', views.movie_detailed_view),
    path('directors/', views.director_all_view),
    path('directors/<int:id_>', views.director_detail_view),
    path('reviews/', views.review_all_view),
    path('reviews/<int:id_>', views.review_detail_view)
]