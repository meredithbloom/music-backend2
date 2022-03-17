from django.db import models



# Create your models here.
class UserAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default='default@gmail.com')
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=1000)

    



    