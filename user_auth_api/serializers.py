from rest_framework import serializers, fields

from .models import Account, UserAccount


#allows you to create and check passwords
from django.contrib.auth.hashers import make_password, check_password

#converts python in models to JSON
class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id', 'name', 'username', 'password')


       # hashes a new user's password when they create an account
    def create(self, validated_data):
        print(self)
        user = UserAccount.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user

    #ensure that an updated password is hashed
    def update(self, instance, validated_data):
        #print(self)
        #print(instance)
        user = UserAccount.objects.get(username=validated_data['username'])
        user.name = validated_data['name']
        user.password = make_password(validated_data['password'])
        user.save()
        return user


class AccountSerializer(serializers.ModelSerializer):
    # serializers.ModelSerializer just tells django to convert sql to JSON
    # owner = UserAccountSerializer(read_only = True)
    class Meta:
        model = Account # tell django which model to use
        fields = ('owner', 'location', 'favorite_genres', 'image') # tell django which fields to include
<<<<<<< HEAD

    
    
=======
>>>>>>> 9683c4c65c5e737936c3f2d4e5864b3004a0327e
