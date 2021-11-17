from django.db import models
from rest_framework import serializers

from .models import Movie, Genre

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
<<<<<<< Updated upstream
        fields = ('id', 'title' ,'poster_path',)
=======
        fields = ('id', 'poster_path',)
>>>>>>> Stashed changes

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'