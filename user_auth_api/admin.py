from django.contrib import admin
from django.contrib.postgres.fields import ArrayField

from .models import UserAccount
admin.site.register(UserAccount)

# Register your models here.
from .models import Account
admin.site.register(Account)
