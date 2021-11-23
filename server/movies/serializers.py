from django.db import models
from rest_framework import serializers

from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    
    youtube_url = serializers.CharField(source='get_youtube_url', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title' ,'poster_path','youtube_url')

class MovieListSerializer(serializers.ModelSerializer):

    youtube_url = serializers.CharField(source='get_youtube_url', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title' ,'poster_path','youtube_url')

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'