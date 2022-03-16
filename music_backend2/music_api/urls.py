from django.urls import path
from . import views

urlpatterns = [
    path('api/songs', views.SongList.as_view(), name='song_list'), # api/contacts will be routed to the ContactList view for handling
    path('api/songs/<int:pk>', views.SongDetail.as_view(), name='song_detail'), # api/contacts will be routed to the ContactDetail view for handling
]
