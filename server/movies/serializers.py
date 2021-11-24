from django.db import models
from rest_framework import serializers

from .models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    
    class GenreSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Genre
            fields = '__all__'

    youtube_url = serializers.CharField(source='get_youtube_url', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title' ,'poster_path', 'overview','youtube_url', 'release_date', 'vote_average', 'genres')

class MovieListSerializer(serializers.ModelSerializer):

    class GenreSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Genre
            fields = '__all__'

    # youtube_url = serializers.CharField(source='get_youtube_url', read_only=True)

    class Meta:
        model = Movie
        fields = ('id', 'title' ,'poster_path','overview', 'release_date', 'vote_average',)

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'