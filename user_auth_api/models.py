from django.db import models



# Create your models here.
class User(models.Model):
    USER_TYPES = (
        ('M', 'Musician'),
        ('L', 'Listener'),
    )
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='default@gmail.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='L')
    



    