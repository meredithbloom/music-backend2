from rest_framework import serializers
from .models import User



#converts python in models to JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ('id', 'name', 'username', 'password')