from django.shortcuts import render
from AdminPanel.models import *

# Create your views here.


def room(request):
    rooms=Rooms.objects.all()

    return render(request,'UserHome/rooms.html',{'rooms':rooms})

def viewroom(request,id):
    room=Rooms.objects.get(id=id)

    return render(request,'UserHome/room.html',{'room':room})