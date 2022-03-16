from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    genre_choices = [
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('techno', 'Techno'),
        ('hiphop', 'Hip-hop'),
        ('jazz', 'Jazz'),
        ('rap', 'Rap'),
        ('country', 'Country'),
        ('metal', 'Metal'),
        ('alternative', 'Alternative'),
        ('indie', 'Indie'),
    ]
    genre = models.CharField(max_length = 100, choices=genre_choices, default='POP')
    audio = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
