

from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.views import login, logout


urlpatterns = [

    path('api/accounts', views.AccountList.as_view(), name='account_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/accounts/<int:pk>', views.AccountDetail.as_view(), name='account_detail'), # api/contacts will be routed to the ContactDetail view for handling

    # api/users will be routed to the UserAccountList for handling
    path('api/useraccount', views.UserAccountList.as_view(), name='useraccount_list'),

    #api/users/:id will be routed to the UserAccountDetails for handling
    path('api/useraccount/<int:pk>', views.UserAccountDetail.as_view(), name='useraccount_detail'),

    #api/users/login will be routed to check_login for handling
    path('api/useraccount/login', csrf_exempt(views.check_login), name='check_login')

]
