from django.shortcuts import render

from rest_framework import generics
from .serializers import UserSerializer
from .models import User 

#allows you to create and check passwords
from django.contrib.auth.hashers import make_password, check_password

#allows you to send json as a response
from django.http import JsonResponse

#allows you to translate dictionaries into json data
import json


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
    
    
# this is the function that checks auth
def check_login(request):
    #if a get request is made, return an empty {}
    if request.method == 'GET':
        return JsonResponse({})
    
    #if a put request is made
    if request.method == 'PUT':
        #make the request json format
        jsonRequest = json.loads(request.body)
        username = jsonRequest['username'] #get username from the request
        password = jsonRequest['password'] #get password from the request
        if User.objects.get(username=username): # see if username exists in db
            user = User.objects.get(username=username) #find user objects with matching username
            
            if check_password(password, user.password): #check if passwords match
                #if passwords match, return a user dictionary/objects
                return JsonResponse({'id': user.id, 'username': user.username, 'name': user.name})
            else: # passwords don't match, return an empty dictionary
                return JsonResponse({})
        else: #if username doesn't exist in db, return an empty dictionary
            return JsonResponse({})
        