from django.urls import path
from . import views



urlpatterns = [
    # api/users will be routed to the UserList for handling
    path('api/users', views.UserList.as_view(), name='useraccount_list'),
    
    #api/users/:id will be routed to the UserDetails for handling
    path('api/users/<int:pk>', views.UserDetail.as_view(), name='useraccount_detail')
]