from rest_framework import serializers
from .models import User



#allows you to create and check passwords
from django.contrib.auth.hashers import make_password, check_password

#converts python in models to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'name', 'username', 'password')
        
    # hashes a new user's password when they create an account
    def create(self, validated_data):
        print(self)
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user 

    # this makes sure their updated passwords are also hashed
    def update(self, instance, validated_data):
        #print(self)
        #print(instance)
        user = User.objects.get(
            username=validated_data['username']
        )
        user.name = validated_data['name']
        user.password = make_password(validated_data['password'])
        user.save()
        return user