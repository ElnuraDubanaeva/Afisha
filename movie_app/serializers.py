from rest_framework import serializers
from .models import Movie, Director, Review


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        # fields = '__all__' to include all fields
        # exclude = 'director'.split() excludes director cant have exclude and fields together have to choose one
        fields = 'id title director'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = 'id movie'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()

    class Meta:
        model = Review
        fields = 'id text movie'.split()
