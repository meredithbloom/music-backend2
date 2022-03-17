from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    # api/users will be routed to the UserList for handling
    path('api/users', views.UserList.as_view(), name='useraccount_list'),

    #api/users/:id will be routed to the UserDetails for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='useraccount_detail'),

    #api/users/login will be routed to check_login for handling
    path('api/users/login', csrf_exempt(views.check_login), name='check_login'),

    path('api/accounts', views.AccountList.as_view(), name='account_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/accounts/<int:pk>', views.AccountDetail.as_view(), name='account_detail'), # api/contacts will be routed to the ContactDetail view for handling

]
