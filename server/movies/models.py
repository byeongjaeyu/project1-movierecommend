from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True, null=True)
    popularity = models.FloatField(blank=True, null=True)
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField(blank=True, null=True)
    poster_path = models.CharField(max_length=200, blank=True,null=True) 
    genres = models.ManyToManyField(Genre)
