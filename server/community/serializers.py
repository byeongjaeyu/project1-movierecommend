from django.db import models
from rest_framework import serializers
from .models import Review, Comment

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('__all__')

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('id', 'title', 'movie_title', 'created_at', 'user')

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('__all__')
