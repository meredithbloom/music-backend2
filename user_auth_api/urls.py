from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.views import login, logout 


urlpatterns = [
    # api/users will be routed to the UserAccountList for handling
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),
    
    #api/users/:id will be routed to the UserAccountDetails for handling
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),
    
    #api/users/login will be routed to check_login for handling
    path('api/useraccount/login', csrf_exempt(views.check_login), name='check_login')
    
]
