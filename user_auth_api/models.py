from django.db import models

# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='default@gmail.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)


class Account(models.Model):
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank = True)
    location = models.CharField(max_length=100, blank = True)
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
    favoritegenre = models.CharField(max_length = 100, choices=genre_choices, default='', blank = True)
    image = models.CharField(max_length = 100, blank = True)
