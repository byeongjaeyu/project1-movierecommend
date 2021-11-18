from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_index),
    path('recommend1/', views.random_recommend),
    path('search/<str:word>/', views.movie_search),
    path('recommend2/<int:movie_id>/', views.choice_recommend),
]
