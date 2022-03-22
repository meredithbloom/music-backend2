from django.shortcuts import render

from rest_framework import generics

from .models import Account
from .serializers import AccountSerializer
from .serializers import UserAccountSerializer
from .models import UserAccount


#allows you to create and check passwords
from django.contrib import auth
from django.contrib.auth.hashers import make_password, check_password

#allows you to send json as a response
from django.http import JsonResponse


#allows you to translate dictionaries into json data
import json


# Create your views here.

# generics.ListCreateAPIView
# GET /users
# POST /users
class UserAccountList(generics.ListCreateAPIView):
    #tells django how to retrieve all objects from the db, ordered by id
    queryset = UserAccount.objects.all().order_by('id')
    #tells django what serializer to use
    serializer_class = UserAccountSerializer


# generics.RetrieveUpdateDestroyAPIView
# GET /users/:id
# DELETE /users/:id
# PUT /users/:id
class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all().order_by('owner') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = AccountSerializer # tell django what serializer to use


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all().order_by('owner')
    serializer_class = AccountSerializer





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
        if UserAccount.objects.get(username=username): # see if username exists in db
            user = UserAccount.objects.get(username=username) #find user objects with matching username

            if check_password(password, user.password): #check if passwords match
                #if passwords match, return a user dictionary/objects & set session object
                request.session['id'] = 'id'
                # auth.login(request, user)

                return JsonResponse({'id': user.id, 'username': user.username, 'name': user.name})
            else: # passwords don't match, return an empty dictionary
                return JsonResponse({})
        else: #if username doesn't exist in db, return an empty dictionary
            return JsonResponse({})


# logout function
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect("/useraccount/loggedout/")
    #redirect to success page
