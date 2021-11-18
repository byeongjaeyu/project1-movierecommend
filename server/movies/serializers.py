from django.db import models
from rest_framework import serializers

from .models import Movie, Genre

class MovieSerializer(serializers.ModelSerializer):
    
    genres = serializers.ListField()
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title' ,'poster_path', 'movie_id',)

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'