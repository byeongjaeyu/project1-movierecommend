from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_index),
    path('recommend/', views.movie_recommend),

]
