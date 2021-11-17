from django.shortcuts import render, get_list_or_404, get_object_or_404
<<<<<<< Updated upstream
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests
from bs4 import BeautifulSoup
# Create your views here.

key = "733c7d5145ecf236ad387093e2d52047"

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_index(request):
    if request.method == 'GET':
        temp = []
        baseUrl = "https://api.themoviedb.org/3/trending/movie/week?api_key="
        Url = baseUrl + key + '&language=ko-kr'
        responses = requests.get(Url).json()
        for response in responses["results"]:
            temp_dict = {}
            temp_dict["title"] = response["title"]
            temp_dict["release_date"] = response["release_date"]
            temp_dict["popularity"] = response["popularity"]
            temp_dict["vote_count"] = response["vote_count"]
            temp_dict["vote_average"] = response["vote_average"]
            temp_dict["overview"] = response["overview"]
            temp_dict["poster_path"] = response["poster_path"]
            temp_dict["genres"] = response["genre_ids"]
            temp.append(temp_dict)
        serializer = MovieListSerializer(temp, many=True)
=======
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
>>>>>>> Stashed changes
        return Response(serializer.data)