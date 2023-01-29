from django.db import models

CHOICES = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


# Create your models here.
class Director(models.Model):
    name = models.CharField(max_length=40)

    @property
    def count(self):
        count = self.movie_director.count()
        return count

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(default=0)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, default='', related_name='movie_director',
                                 null=True, blank=True)

    @property
    def rating(self):
        count = self.movie_review.count()
        if count == 0:
            return 0
        total = 0
        for i in self.movie_review.all():
            total += i.stars
        return total / count

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(null=True, blank=True, default='')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_review')
    stars = models.IntegerField(choices=CHOICES, default=0)

    def __str__(self):
        return self.text
