from django.db import models


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, default='', related_name='movie_director',
                                 null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')

    def __str__(self):
        return self.text
