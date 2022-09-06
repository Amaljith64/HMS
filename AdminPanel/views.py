from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
from AccountSection.models import *
from django.core.paginator import Paginator
from django.db.models.functions import *
from django.db.models import *
import calendar
from datetime import date
from Payments.models import PaymentClass
import datetime

# Create your views here.


# def index(request):

   

#     return render(request, 'AdminPanel/index.html')




#------------------------------------ROOM------------------------------#



def addrooms(request):
    scateg=SubCategories.objects.all
    categ=Categories.objects.all

    if request.method=='POST':



        name=request.POST.get('hotel_name')
       
        price=request.POST.get('price')
        Desc=request.POST['description']
        image=request.FILES['photoo']
        multiimages = request.FILES.getlist('images')
        categ=Categories.objects.get(id=request.POST['categ'])
        scateg=SubCategories.objects.get(id=request.POST['scateg'])
        
        # print(location)

        addroom=Rooms.objects.create(img=image,categ=categ,subcateg=scateg,name=name,Desc=Desc,price=price)
        addroom.save()

        for multiimage in multiimages:
            photo = MultiImage(imageof=addroom)
            
            photo.image=multiimage
            photo.save()

        return redirect(rooms)
     
    return render(request,'AdminPanel/add-room.html',{'categ':categ,'scateg':scateg})

def rooms(request):

    rooms=Rooms.objects.all()
    paginator=Paginator(rooms,per_page=6)
    page_number=request.GET.get('page')
    roomsFinal=paginator.get_page(page_number)
    totalpage=roomsFinal.paginator.num_pages
    context={
        'rooms':roomsFinal,
        'lastpage':totalpage,
        'totalPagelist':[ n+1 for n  in range(totalpage)]

    }

    return render(request,'AdminPanel/room-list.html',context)


def deleteroom(request,id):
    rooms=Rooms.objects.all()
    room=Rooms.objects.get(id=id)
    room.delete()
    return render(request, 'AdminPanel/xml-room-list.html', {'rooms':rooms})



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


#------------------------------------ROOM ENDS------------------------------#




#------------------------------------CATEGORY------------------------------#


def category(request):
    if request.method =='POST':
        title=request.POST['title']
        description=request.POST['description']
        cat=Categories(title=title,description=description)
        if Categories.objects.filter(title__icontains=title).exists():
                messages.error(request, "This Category already Exists")
                print('This category exits')
                return redirect(category)
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
        if SubCategories.objects.filter(title__icontains=title).exists():
                messages.error(request, "This SubCategory already Exists")
                print('This subcategory exits')
                return redirect(subcategory)
        cat=SubCategories(category_id=maincatid,title=title,description=description)
        cat.save()
        return redirect(subcategory)
    scateg=SubCategories.objects.all()
    return render(request,'AdminPanel/subcategory.html',{'scateg':scateg,'categ':categ})




#------------------------------------CATEGORY ENDS------------------------------#





#------------------------------------USER------------------------------#




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


#------------------------------------USER ENDS------------------------------#


#------------------------------------BOOKINGS------------------------------#


def bookings(request):
    bookings=HotelBookings.objects.all()
    return render(request,'AdminPanel/Bookings.html',{'bookings':bookings})





#------------------------------------BOOKINGS ENDS------------------------------#
 








def index(request):

    orders=HotelBookings.objects.annotate(month=ExtractMonth('created_at')).values('month').annotate(count=Count('id')).values('month','count')
    yearorders=HotelBookings.objects.annotate(year=ExtractYear('created_at')).values('year').annotate(count=Count('id')).values('year','count')
    Dayorders=HotelBookings.objects.annotate(day=ExtractDay('created_at')).filter(created_at=date.today()).values('day').annotate(count=Count('id')).values('day','count')

    print(Dayorders)
    DayNumber=[]
    YearNumber=[]
    monthNumber=[]
    totalOrders=[]
    totaltyearorders=[]
    totaldayorder=[]
    for d in orders:
        monthNumber.append(calendar.month_name[d['month']])
        totalOrders.append(d['count'])

    for d in yearorders:
        YearNumber.append([d['year']])
        totaltyearorders.append(d['count'])
    
    for d in Dayorders:
        DayNumber.append([d['day']])
        totaldayorder.append(d['count'])

    # ---------------------------------- payment --------------------------------- #
    

    payathotel = PaymentClass.objects.filter(payment_method = 'Pay At Hotel').aggregate(Count('id')).get('id__count')
       
    raz = PaymentClass.objects.filter(payment_method = 'Razorpay').aggregate(Count('id')).get('id__count')

    pay = PaymentClass.objects.filter(payment_method = 'Paypal').aggregate(Count('id')).get('id__count')


    

    
    context={
        'Order':orders,
        'MonthNumber':monthNumber,
        'TotalOrders':totalOrders,
        'YearNumber':YearNumber,
        'totaltyearorders':totaltyearorders,
        'DayNumber':DayNumber,
        'totaldayorder':totaldayorder,
        'paypal':pay,
        'raz':raz,
        'cod':payathotel

    }

    return render(request,'AdminPanel/index.html',context)




def add_coupons(request):
    coupons=Coupons.objects.all()
    if request.method=="POST":
        coupon=request.POST['code']
        valid_to=request.POST['validity']
        discount=request.POST['discount']
        coupon_code=Coupons.objects.create(coupon_code=coupon,valid_to=valid_to,discount=discount)

    return render(request,'AdminPanel/coupons.html',{'coupons':coupons})






  