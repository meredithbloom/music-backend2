from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import SongSerializer
from .models import Song

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = SongSerializer # tell django what serializer to use

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer
