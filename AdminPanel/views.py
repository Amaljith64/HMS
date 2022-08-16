from django.shortcuts import render,redirect
from . models import *

# Create your views here.


def rooms(request):

    rooms=Rooms.objects.all()

    return render(request,'AdminPanel/room-list.html',{'rooms':rooms})





def addrooms(request):
    # location=Location.objects.all
    type=Roomtype.objects.all

    if request.method=='POST':



        name=request.POST.get('hotel_name')      
        # location=Location.objects.get(id=request.POST['loc'])
        price=request.POST.get('price')
        Desc=request.POST['description']
        image=request.FILES['photoo']
        type=Roomtype.objects.get(id=request.POST['type'])
        
        # print(location)

        addroom=Rooms.objects.create(img=image,Roomtype=type,name=name,Desc=Desc,price=price)
        addroom.save()

        return redirect(rooms)
     
    return render(request,'AdminPanel/add-room.html',{'type':type})
