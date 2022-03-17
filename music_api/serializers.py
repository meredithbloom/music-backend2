from rest_framework import serializers
from .models import Song

class SongSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Song # tell django which model to use
        fields = ('id', 'name', 'artist', 'genre', 'audio', 'image', 'price', 'release_type') # tell django which fields to include
