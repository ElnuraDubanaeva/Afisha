from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, MovieDetailSerializer, DirectorSerializer, DirectorDetailSerializer, \
    ReviewSerializer, ReviewDetailSerializer
from .models import Movie, Director, Review
from rest_framework import status


@api_view(['GET'])
def movie_all_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_detailed_view(request, id_):
    try:
        movie = Movie.objects.get(id=id_)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieDetailSerializer(movie, many=False)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_all_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_detail_view(request, id_):
    try:
        director = Director.objects.get(id=id_)
    except Director.DoesNotExist:
        return Response(data={'error': 'director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorDetailSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_all_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_detail_view(request, id_):
    try:
        review = Review.objects.get(id=id_)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewDetailSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movie_review_view(request):
    reviews = Movie.objects.all()
    serializer = MovieDetailSerializer(reviews, many=True)
    return Response(data=serializer.data)
