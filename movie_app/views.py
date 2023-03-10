from rest_framework.response import Response
from .serializers import MovieSerializer, MovieDetailSerializer, DirectorSerializer, DirectorDetailSerializer, \
    ReviewSerializer, ReviewDetailSerializer, MovieValidateSerializer, DirectorValidateSerializer, \
    ReviewValidateSerializer
from .models import Movie, Director, Review
from rest_framework import status
from rest_framework.viewsets import ModelViewSet


class MovieAllViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def create(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data=MovieSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


# @api_view(['GET', 'POST'])
# def movie_all_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         title = serializer.validated_data.get('title')
#         description = serializer.validated_data.get('description')
#         duration = serializer.validated_data.get('duration')
#         director_id = serializer.validated_data.get('director_id')
#         movie = Movie.objects.create(title=title, description=description, duration=duration,
#                                      director_id=director_id)
#         movie.save()
#         return Response(data=MovieSerializer(movie).data,
#                         status=status.HTTP_201_CREATED)


class MovieDetailViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        duration = serializer.validated_data.get('duration')
        description = serializer.validated_data.get('description')
        director_id = serializer.validated_data.get('director_id')
        movie = Movie.objects.all()
        movie.title = title
        movie.duration = duration
        movie.description = description
        movie.director_id = director_id
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detailed_view(request, id_):
#     try:
#         movie = Movie.objects.get(id=id_)
#     except Movie.DoesNotExist:
#         return Response(data={'error': 'Movie not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MovieDetailSerializer(movie, many=False)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(data=MovieDetailSerializer(movie).data,
#                         status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = MovieValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         title = serializer.validated_data.get('title')
#         duration = serializer.validated_data.get('duration')
#         description = serializer.validated_data.get('description')
#         director_id = serializer.validated_data.get('director_id')
#         movie.title = title
#         movie.duration = duration
#         movie.description = description
#         movie.director_id = director_id
#         movie.save()
#         return Response(data=MovieDetailSerializer(movie).data,
#                         status=status.HTTP_201_CREATED)


class DirectorAllViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

    def create(self, request, *args, **kwargs):
        serializer = DirectorSerializer(data=request.data)
        name = serializer.validated_data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorSerializer(director).data,
                        status=status.HTTP_201_CREATED)


#
# @api_view(['GET', 'POST'])
# def director_all_view(request):
#     if request.method == 'GET':
#         directors = Director.objects.all()
#         serializer = DirectorSerializer(directors, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = DirectorValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         name = serializer.validated_data.get('name')
#         director = Director.objects.create(name=name)
#         director.save()
#         return Response(data=DirectorSerializer(director).data,
#                         status=status.HTTP_201_CREATED)

class DirectorDetailViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorDetailSerializer
    lookup_field = 'id'

    def create(self, request, *args, **kwargs):
        serializer = DirectorValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        director = Director.objects.all()
        director.name = name
        director.save()
        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


# @api_view(['GET', 'PUT', 'DELETE'])
# def director_detail_view(request, id_):
#     try:
#         director = Director.objects.get(id=id_)
#     except Director.DoesNotExist:
#         return Response(data={'error': 'director not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = DirectorDetailSerializer(director)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = DirectorValidateSerializer(data=request.data)
#         name = serializer.validated_data.get('name')
#         director.name = name
#         director.save()
#         return Response(data=DirectorDetailSerializer(director).data,
#                         status=status.HTTP_201_CREATED)

class ReviewAllViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')
        reviews = Review.objects.all(text=text, stars=stars, movie_id=movie_id)
        return Response(data=ReviewSerializer(reviews).data,
                        status=status.HTTP_201_CREATED)


#
# @api_view(['GET', 'POST'])
# def review_all_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(data=serializer.data)
#     else:
#         serializer = ReviewValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#         movie_id = serializer.validated_data.get('movie_id')
#         reviews = Review.objects.all(text=text, stars=stars, movie_id=movie_id)
#         return Response(data=ReviewSerializer(reviews).data,
#                         status=status.HTTP_201_CREATED)

class ReviewDetailViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewDetailSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        stars = serializer.validated_data.get('stars')
        movie_id = serializer.validated_data.get('movie_id')
        review = Review.objects.all()
        review.text = text
        review.stars = stars
        review.movie_id = movie_id
        review.save()
        return Response(data=ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


#
# @api_view(['GET', 'PUT', 'DELETE'])
# def review_detail_view(request, id_):
#     try:
#         review = Review.objects.get(id=id_)
#     except Review.DoesNotExist:
#         return Response(data={'error': 'review not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = ReviewDetailSerializer(review)
#         return Response(data=serializer.data)
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         text = serializer.validated_data.get('text')
#         stars = serializer.validated_data.get('stars')
#         movie_id = serializer.validated_data.get('movie_id')
#         review.text = text
#         review.stars = stars
#         review.movie_id = movie_id
#         review.save()
#         return Response(data=ReviewDetailSerializer(review).data,
#                         status=status.HTTP_201_CREATED)
#
class MovieReviewViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer

# @api_view(['GET'])
# def movie_review_view(request):
#     reviews = Movie.objects.all()
#     serializer = MovieDetailSerializer(reviews, many=True)
#     return Response(data=serializer.data)
