from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.html',{})


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })