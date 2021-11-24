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
youtube_base_url = 'https://www.youtube.com/watch?v='




@api_view(['GET'])
@permission_classes([AllowAny])
def movie_index(request):
    if request.method == 'GET':
        videoUrl = ["Pj7CadRf82k", "uiIIyepK6XY", "5EbdgThNoiM", "-5Dc8EMVYBo", "TJyQYnf-6lE", "BryJA-Xp-Q4",
        "iXfbMtMI8R0", "BdkSkI61aGo", "yFZh-Wqi7RI", "eqn0Hj1e3jg", '', "xDmRI9y0LEs", "lWGuFIeTkw4", "dP57Rnzr2M0", "n9_v7L7t51c", "AMAS18DUgAw",
        "4rTkrtH2s3o", "rmR7xefwjWs", "6R143jGPmcQ", "UeK8MG5tGkQ"]
        temp = []
        baseUrl = "https://api.themoviedb.org/3/trending/movie/week?api_key="
        Url = baseUrl + key + '&language=ko-kr'
        responses = requests.get(Url).json()
        idx = 0
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
            temp_dict["youtube_url"] = youtube_base_url + videoUrl[idx]
            temp.append(temp_dict)
            idx += 1
        return Response(temp)


@api_view(['GET'])
@permission_classes([AllowAny])
def random_recommend(request):
    video_url = 'https://api.themoviedb.org/3/movie/'
    video_url2 = f'/videos?api_key={key}&language=ko-kr'
    search_url = 'https://api.themoviedb.org/3/search/movie?api_key=733c7d5145ecf236ad387093e2d52047&language=ko-kr&query='
    if request.method == 'GET':
        movie_list = []
        movies = Movie.objects.all()
        ran_index = random.sample(range(1,len(movies)), 10)
        for idx in ran_index:
            movie_list.append(movies[idx])
        for movie in movie_list:
            print(type(movie))
            searchUrl = search_url + movie.title
            responses = requests.get(searchUrl).json()
            movie_id = responses["results"][0]["id"]
            videoUrl = video_url + str(movie_id) + video_url2
            responses = requests.get(videoUrl).json()
            if not responses["results"]:
                movie.set_youtube_url('')
            else:
                for video in responses['results']:
                    if video["type"] == 'Trailer':
                        youtubeUrl = youtube_base_url + video["key"]
                        movie.set_youtube_url(youtubeUrl)
                        break
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
                movieList = movies.order_by('vote_average')[:10]
            else:
                movies = Movie.objects.all()
                movieList = movies.order_by('vote_average')[:10]
        else:
            movies = Movie.objects.all()
            movieList = movies.order_by('vote_average')[:10]
        for movie in movieList:
            movie_list.append(movie)
        video_url = 'https://api.themoviedb.org/3/movie/'
        video_url2 = f'/videos?api_key={key}&language=ko-kr'
        search_url = 'https://api.themoviedb.org/3/search/movie?api_key=733c7d5145ecf236ad387093e2d52047&language=ko-kr&query='
        for movie in movie_list:
            searchUrl = search_url + movie.title
            responses = requests.get(searchUrl).json()
            movie_id = responses["results"][0]["id"]
            videoUrl = video_url + str(movie_id) + video_url2
            responses = requests.get(videoUrl).json()
            print(videoUrl)
            if not responses["results"]:
                movie.set_youtube_url('')
            else:
                for video in responses['results']:
                    if video["type"] == 'Trailer':
                        youtubeUrl = youtube_base_url + video["key"]
                        movie.set_youtube_url(youtubeUrl)
                        break
    
    serializer = MovieSerializer(movie_list, many=True)
    return Response(serializer.data)

# @api_view(['GET'])
# @permission_classes([AllowAny])
# def movie_search(request, word):
#     if request.method == 'GET':
#         Url = f"https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-kr&query={word}&page=1&include_adult=false"
#         responses = requests.get(Url).json()
#         temp = []
#         pages = responses["total_pages"]
#         check = responses["total_results"]
#         if check != 0:
#             for page in range(1,2):
#                 Url = f"https://api.themoviedb.org/3/search/movie?api_key={key}&language=ko-kr&query={word}&page={page}&include_adult=false"
#                 responses = requests.get(Url)
#                 soup = BeautifulSoup(responses.text, 'html.parser')
#                 print(soup)
#                 for response in responses["results"]:
#                     temp_dict = {}
#                     try:
#                         temp_dict["movie_id"] = response["id"]
#                         temp_dict["title"] = response["title"]
#                         temp_dict["release_date"] = response["release_date"]
#                         temp_dict["popularity"] = response["popularity"]
#                         temp_dict["vote_count"] = response["vote_count"]
#                         temp_dict["vote_average"] = response["vote_average"]
#                         temp_dict["overview"] = response["overview"]
#                         temp_dict["poster_path"] = poster_url + str(response["poster_path"])
#                         temp_dict["genres"] = response["genre_ids"]
#                         temp.append(temp_dict)
#                     except KeyError:
#                         continue
#         serializer = MovieSerializer(temp, many=True)
#         return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_search(request, word):
    if request.method == 'GET':
        movies = Movie.objects.all()
        movie_list = []
        for movie in movies:
            if word in movie.title:
                movie_list.append(movie)
        movie_list = movie_list[:40]
        serializer = MovieListSerializer(movie_list, many=True)
        return Response(serializer.data)

# https://www.youtube.com/watch?v=AMWUjwM07g4"
