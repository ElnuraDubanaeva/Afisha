from rest_framework import serializers
from .models import Movie, Director, Review


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        # fields = '__all__' to include all fields
        # exclude = 'director'.split() excludes director cant have exclude and fields together have to choose one
        fields = 'id title director'.split()

    def get_director(self, instance):
        return instance.director.__str__()


class MovieDetailSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = 'id title description duration director'.split()

    def get_director(self, instance):
        return instance.director.__str__()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id movie'.split()

    def get_movie(self, instance):
        return instance.movie.__str__()


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = 'id text movie'.split()

    def get_movie(self, instance):
        return instance.movie.__str__()
