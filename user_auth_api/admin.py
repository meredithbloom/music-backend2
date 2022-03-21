from django.contrib import admin
from django.contrib.postgres.fields import ArrayField 



# Register your models here.
from .models import UserAccount
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['favorite_genres']


admin.site.register(UserAccount)
admin.site.register(Account, AccountAdmin)



