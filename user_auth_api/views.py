from django.shortcuts import render

from rest_framework import generics
from .serializers import UserSerializer
from .models import User 



# Create your views here.


# generics.ListCreateAPIView
# GET /users
# POST /users
class UserList(generics.ListCreateAPIView):
    #tells django how to retrieve all objects from the db, ordered by id
    queryset = User.objects.all().order_by('id')
    #tells django what serializer to use
    serializer_class = UserSerializer


# generics.RetrieveUpdateDestroyAPIView
# GET /users/:id
# DELETE /users/:id
# PUT /users/:id

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer