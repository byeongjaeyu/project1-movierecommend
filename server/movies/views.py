from django.shortcuts import render, get_list_or_404, get_object_or_404
import requests
from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
import requests
import random
from bs4 import BeautifulSoup
from community.models import Review
# Create your views here.

key = "733c7d5145ecf236ad387093e2d52047"
poster_url = "https://image.tmdb.org/t/p/original/"
youtube_base_url = 'https://www.youtube.com/embed/'



@api_view(['GET'])
@permission_classes([AllowAny])
def movie_index(request):
    if request.method == 'GET':
        movie_list = []
        movies = Movie.objects.all()
        movielist = movies.order_by('-release_date')
        cnt = 1
        for movie in movielist:
            if movie.youtube_url:
                movie_list.append(movie)
                cnt += 1
            if cnt == 20:
                break
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def random_recommend(request):
    if request.method == 'GET':
        movie_list = []
        movies = Movie.objects.all()
        ran_index = random.sample(range(1,len(movies)), 20)
        for idx in ran_index:
            movie_list.append(movies[idx])
        serializer = MovieSerializer(movie_list, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def genre_recommend(request):
    if request.method == 'POST':
        userId = int(list(request.data.keys())[0])
        reviews = Review.objects.filter(user_id=userId)
        like_genre = set()
        movie_list = []
        random_list = []
        if reviews.count():
            for review in reviews:
                movie = Movie.objects.filter(title=review.movie_title)
                if movie.exists():
                    genres = movie[0].genres.all()
                    for genre in genres:
                        like_genre.add(genre.id)
            movies = Movie.objects.none()
            if like_genre:
                for genre in like_genre:
                    movie = Movie.objects.filter(genres__in=[genre])
                    movies = movies.union(movie, all=False)
                movieList = movies.order_by('vote_average')[:100]
            else:
                movies = Movie.objects.all()
                movieList = movies.order_by('vote_average')[:100]
        else:
            movies = Movie.objects.all()
            movieList = movies.order_by('vote_average')[:100]
        for movie in movieList:
            movie_list.append(movie)
    ran_index = random.sample(range(1,len(movie_list)), 20)
    for idx in ran_index:
        random_list.append(movie_list[idx])
    serializer = MovieSerializer(random_list, many=True)
    return Response(serializer.data)



@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search(request, word):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_list = []
        for movie in movies:
            if word in movie.title:
                movie_list.append(movie)
        serializer = MovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

# https://www.youtube.com/watch?v=AMWUjwM07g4"
