from django.shortcuts import render, redirect

from . models import *
from AccountSection.models import *

# Create your views here.


def index(request):

   

    return render(request, 'AdminPanel/index.html')


def addrooms(request):
    scateg=SubCategories.objects.all
    categ=Categories.objects.all

    if request.method=='POST':



        name=request.POST.get('hotel_name')      
       
        price=request.POST.get('price')
        Desc=request.POST['description']
        image=request.FILES['photoo']
        categ=Categories.objects.get(id=request.POST['categ'])
        scateg=SubCategories.objects.get(id=request.POST['scateg'])
        
        # print(location)

        addroom=Rooms.objects.create(img=image,categ=categ,subcateg=scateg,name=name,Desc=Desc,price=price)
        addroom.save()

        return redirect(rooms)
     
    return render(request,'AdminPanel/add-room.html',{'categ':categ,'scateg':scateg})

def rooms(request):

    rooms=Rooms.objects.all()

    return render(request,'AdminPanel/room-list.html',{'rooms':rooms})


def editroom(request,id):
    # location=Location.objects.all
    type=Categories.objects.all
    room=Rooms.objects.get(id=id)
    
    if request.method=='POST':
        

        name=request.POST['hotel_name']
        # location=Location.objects.get(id=request.POST['loc'])
        price=request.POST['price']
        Desc=request.POST['description']
        type=Categories.objects.get(id=request.POST['type'])
        room.name=name
        # room.Location=location
        room.Roomtype=type
        room.Desc=Desc
        room.price=price

        room.save()
    
       
        print('saved')
        return redirect(rooms)

    return render(request,'AdminPanel/edit-room.html',{'room':room,'type':type})

def deleteroom(request,id):
    room=Rooms.objects.get(id=id)
    room.delete()
    return redirect(rooms)


def category(request):
    if request.method =='POST':
        title=request.POST['title']
        description=request.POST['description']
        cat=Categories(title=title,description=description)
        cat.save()
        return redirect(category)
    categ=Categories.objects.all()
    return render(request,'AdminPanel/category.html',{'categ':categ})

def subcategory(request):
    categ=Categories.objects.all()
    if request.method =='POST':
        maincatid=Categories.objects.get(id=request.POST['maincategory'])
        # maincatid=request.POST['maincategory']
        title=request.POST['title']
        description=request.POST['description']
        cat=SubCategories(category_id=maincatid,title=title,description=description)
        cat.save()
        return redirect(subcategory)
    scateg=SubCategories.objects.all()
    return render(request,'AdminPanel/subcategory.html',{'scateg':scateg,'categ':categ})


def guest(request):
    if request.method=='POST':
        load=request.POST['search']
        if load !="":
            mydata=Account.objects.filter(username__icontains=load)
            return render(request,'AdminPanel/guest-list.html',{'datas':mydata})
        return redirect(guest)

    else:
        mydata = Account.objects.all()
        return render(request,'AdminPanel/guest-list.html',{'datas': mydata})

def blockuser(request,id):
    user=Account.objects.get(id=id)
    if user.is_active:
        user.is_active = False
        user.save()
        return redirect(guest)
    else:
        user.is_active = True
        user.save()
        return redirect(guest)  