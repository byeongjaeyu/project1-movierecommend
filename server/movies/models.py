from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=True)
    popularity = models.FloatField(null=True)
    runtime = models.IntegerField(null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField(null=True)
    poster_path = models.CharField(max_length=200,null=True) 
    youtube_url = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)

    # def get_youtube_url(self):
    #     return self.youtube_url
    
    # def set_youtube_url(self, url):
    #     self.youtube_url = url
