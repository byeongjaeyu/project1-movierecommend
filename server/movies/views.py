from django.shortcuts import render, get_list_or_404, get_object_or_404
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Movie, Genre
from .serializers import MovieListSerializer, MovieSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
import requests
import random
from bs4 import BeautifulSoup
# Create your views here.

key = "733c7d5145ecf236ad387093e2d52047"
poster_url = "https://image.tmdb.org/t/p/original/"

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
            temp_dict["movie_id"] = response["id"]
            temp_dict["title"] = response["title"]
            temp_dict["release_date"] = response["release_date"]
            temp_dict["popularity"] = response["popularity"]
            temp_dict["vote_count"] = response["vote_count"]
            temp_dict["vote_average"] = response["vote_average"]
            temp_dict["overview"] = response["overview"]
            temp_dict["poster_path"] = poster_url + response["poster_path"]
            temp_dict["genres"] = response["genre_ids"]
            temp.append(temp_dict)
        serializer = MovieListSerializer(temp, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def random_recommend(request):
    if request.method == 'GET':
        ran_num = random.randrange(1,500)
        Url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=ko-kr&include_adult=false&include_video=false&page={ran_num}&with_watch_monetization_types=flatrate"
        temp = []
        responses = requests.get(Url).json()

        for response in responses["results"]:
            temp_dict = {}
            temp_dict["movie_id"] = response["id"]
            temp_dict["title"] = response["title"]
            temp_dict["release_date"] = response["release_date"]
            temp_dict["popularity"] = response["popularity"]
            temp_dict["vote_count"] = response["vote_count"]
            temp_dict["vote_average"] = response["vote_average"]
            temp_dict["overview"] = response["overview"]
            if response["poster_path"]:
                temp_dict["poster_path"] = poster_url + response["poster_path"]
            else:
                temp_dict["poster_path"] = poster_url
            temp_dict["genres"] = response["genre_ids"]
            temp.append(temp_dict)
        serializer = MovieSerializer(temp, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search(request, word):
    if request.method == 'GET':
        Url = f"https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-kr&query={word}&page=1&include_adult=false"
        responses = requests.get(Url).json()
        temp = []
        pages = responses["total_pages"]
        check = responses["total_results"]
        if check != 0:
            for page in range(1,2):
                Url = f"https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-kr&query={word}&page={page}&include_adult=false"
                responses = requests.get(Url)
                soup = BeautifulSoup(responses.text, 'html.parser')
                print(soup)
                for response in responses["results"]:
                    temp_dict = {}
                    try:
                        temp_dict["movie_id"] = response["id"]
                        temp_dict["title"] = response["title"]
                        temp_dict["release_date"] = response["release_date"]
                        temp_dict["popularity"] = response["popularity"]
                        temp_dict["vote_count"] = response["vote_count"]
                        temp_dict["vote_average"] = response["vote_average"]
                        temp_dict["overview"] = response["overview"]
                        temp_dict["poster_path"] = poster_url + str(response["poster_path"])
                        temp_dict["genres"] = response["genre_ids"]
                        temp.append(temp_dict)
                    except KeyError:
                        continue

        serializer = MovieSerializer(temp, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# @permission_classes([AllowAny])
# def genre_recommend(request):
#     if request.user.is_authenticated:
#         user = request.user
#         reviews = user.review_set.all()
#         like_genre = set()
#         if reviews.count():
#             for review in reviews:
#                 movie = Movie.objects.filter(title=review.movie_title)
#                 if movie.exists():
#                     genres = movie[0].genres.all()
#                     for genre in genres:
#                         like_genre.add(genre.id)
#             movies = Movie.objects.none()
#             for genre in like_genre:
#                 movie = Movie.objects.filter(genres__in=[genre])
#                 movies = movies.union(movie, all=False)
#             movie_list = movies.order_by('vote_average')[:10]
#         else:
#             movies = Movie.objects.all()
#             movie_list = movies.order_by('vote_average')[:10]
#         print(movie_list)
#     context = {
#         'movie_list' : movie_list,
#     }
#     return Response(context)


@api_view(['GET'])
@permission_classes([AllowAny])
def dataInput(request):
    if request.method == 'GET':
        for page in range(1,10):
            Url = f"https://api.themoviedb.org/3/discover/movie?api_key={key}&language=ko-kr&include_adult=false&include_video=false&page={page}&with_watch_monetization_types=flatrate"
            temp = []
            responses = requests.get(Url).json()
            for response in responses["results"]:
                    temp_dict = {}
                    try:
                        Movie.objects.create(
                                title=response["title"],
                                release_data=response["release_date"],
                                popularity=response["popularity"],
                                vote_count=response["vote_count"],
                                vote_average=response["vote_average"],
                                overview=response["overview"],
                                poster_path=poster_url + str(response["poster_path"]),
                                genres=response["genre_ids"]
                            )
                        # temp_dict["title"] = response["title"]
                        # temp_dict["release_date"] = response["release_date"]
                        # temp_dict["popularity"] = response["popularity"]
                        # temp_dict["vote_count"] = response["vote_count"]
                        # temp_dict["vote_average"] = response["vote_average"]
                        # temp_dict["overview"] = response["overview"]
                        # temp_dict["poster_path"] = poster_url + str(response["poster_path"])
                        # temp_dict["genres"] = response["genre_ids"]
                        # temp.append(temp_dict)
                    except KeyError:
                        continue

            temp.append(temp_dict)
            serializer = MovieSerializer(temp, many=True)
        return Response(serializer.data)