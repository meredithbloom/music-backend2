from django.contrib import admin
<<<<<<< HEAD
from django.contrib.postgres.fields import ArrayField 


=======
from django.contrib.postgres.fields import ArrayField

from .models import UserAccount
admin.site.register(UserAccount)
>>>>>>> 9683c4c65c5e737936c3f2d4e5864b3004a0327e

# Register your models here.
from .models import UserAccount
from .models import Account


# class AccountAdmin(admin.ModelAdmin):
#     list_display = ('favorite_genres',)


admin.site.register(UserAccount)
admin.site.register(Account)



