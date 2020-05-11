from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.auth.decorators import login_required
import json


# Create your views here.
def index(request):
    return render(request, 'index.html',{})

@login_required
def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name,
        'username': mark_safe(json.dumps(request.user.username)),
    })
