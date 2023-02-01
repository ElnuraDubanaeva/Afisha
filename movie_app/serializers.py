from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Movie, Director, Review


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__' to include all fields
        # exclude = 'director'.split() excludes director cant have exclude and fields together have to choose one
        fields = 'id title director'.split()

    def get_director(self, instance):
        return instance.director.name


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id text movie '.split()

    def get_movie(self, instance):
        return instance.movie.title


class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    review = Review.objects.all()
    movie_review = ReviewDetailSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id title description duration director movie_review rating '.split()

    def get_director(self, instance):
        return instance.director.name


class DirectorSerializer(serializers.ModelSerializer):
    movie_director = MovieSerializer(many=True)

    class Meta:
        model = Director
        fields = 'id name count movie_director'.split()

    def get_movie_director(self, instance):
        return instance.movie.title


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id movie text'.split()

    def get_movie(self, instance):
        return instance.movie.title


class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    description = serializers.CharField()
    duration = serializers.FloatField(min_value=1)
    director_id = serializers.IntegerField(min_value=0)

    def validate_director(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError(f'Director with ({director_id}) does not exists!')
        return director_id


class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField(min_value=0)
    movie_id = serializers.IntegerField(min_value=0)

    def validate_movie(self, movie_id):
        try:
            Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            raise ValidationError(f'Movie with {movie_id} does not exists!')
        return movie_id

    # def validate_tags(self, tags):
    #     len_ =
    #     tags_id = [i[0] for i in Tag.objects.all().values_list('id')]
    #     for t in tags:
    #         if t not in tags_id:
    #             raise ValidationError(f'Tag with ({t}) does not exists!')
    #     return tags
