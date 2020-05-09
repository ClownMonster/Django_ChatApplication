from django.urls import path
from .views import index, room

app_name = 'chat'

urlpatterns = [

    path('', index, name= 'Home' ),
    path('<str:room_name>/', room, name='room')


]