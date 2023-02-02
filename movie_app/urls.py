from django.urls import path
from . import views
urlpatterns = [
    path('movies/', views.MovieAllViewSet.as_view({'get':'list','post':'create'})),
    path('movies/<int:id>', views.MovieDetailViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('directors/', views.DirectorAllViewSet.as_view({'get':'list','post':'create'})),
    path('directors/<int:id>', views.DirectorDetailViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('reviews/', views.ReviewAllViewSet.as_view({'get':'list','post':'create'})),
    path('reviews/<int:id>', views.ReviewDetailViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('movies/reviews',views.MovieReviewViewSet.as_view({'get':'list'}))
]