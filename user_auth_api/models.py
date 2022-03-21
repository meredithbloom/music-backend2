from django.contrib.postgres.fields import ArrayField
from django.db import models



# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='default@gmail.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)






# choices
#(actual value to be set on model, human readable name)


class Account(models.Model):
    owner = models.OneToOneField(UserAccount, related_name='account', on_delete=models.CASCADE, null=True)
    location = models.CharField(max_length=100, default='unknown', blank = True)
    GENRE_CHOICES = [
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
    favorite_genres = ArrayField(
        models.CharField(
            max_length = 1000, choices=GENRE_CHOICES, default=GENRE_CHOICES, blank = True)
    )
    image = models.CharField(max_length = 100, default='https://imgur.com/V4RclNb',  blank = True)
