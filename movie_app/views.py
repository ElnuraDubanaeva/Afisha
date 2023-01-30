from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer, MovieDetailSerializer, DirectorSerializer, DirectorDetailSerializer, \
    ReviewSerializer, ReviewDetailSerializer
from .models import Movie, Director, Review
from rest_framework import status


@api_view(['GET', 'POST'])
def movie_all_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)
    else:
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration,
                                     director_id=director_id)
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detailed_view(request, id_):
    try:
        movie = Movie.objects.get(id=id_)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(data=MovieDetailSerializer(movie).data,
                        status=status.HTTP_204_NO_CONTENT)
    else:
        title = request.data.get('title')
        duration = request.data.get('duration')
        description = request.data.get('description')
        director_id = request.data.get('director_id')
        movie.title = title
        movie.duration = duration
        movie.description = description
        movie.director_id = director_id
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def director_all_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)
    else:
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id_):
    try:
        director = Director.objects.get(id=id_)
    except Director.DoesNotExist:
        return Response(data={'error': 'director not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_all_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    else:
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        reviews = Review.objects.all(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id_):
    try:
        review = Review.objects.get(id=id_)
    except Review.DoesNotExist:
        return Response(data={'error': 'review not found'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        text = request.data.get('text')
        stars = request.data.get('stars')
        movie_id = request.data.get('movie_id')
        review.text = text
        review.stars = stars
        review.movie_id = movie_id
        review.save()
        return Response(data=ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET'])
def movie_review_view(request):
    reviews = Movie.objects.all()
    serializer = MovieDetailSerializer(reviews, many=True)
    return Response(data=serializer.data)
