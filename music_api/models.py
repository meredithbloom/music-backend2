from django.db import models
from user_auth_api.models import User

# Create your models here.
class Song(models.Model):
    name = models.CharField(max_length = 100)
    artist = models.CharField(max_length = 100)
    genre = models.CharField(max_length = 100)
    audio = models.CharField(max_length = 100)
    image = models.CharField(max_length = 100)
