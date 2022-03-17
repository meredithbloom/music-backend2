from django.db import models

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length = 100, blank = True)
    artist = models.CharField(max_length = 100, blank = True)
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
    genre = models.CharField(max_length = 100, choices=genre_choices, default='pop', blank = True)
    audio = models.CharField(max_length = 100, blank = True)
    image = models.CharField(max_length = 100, blank = True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default = '1.29')
