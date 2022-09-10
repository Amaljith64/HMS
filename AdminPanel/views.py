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



def CategoryOffer(request):
    offers=Category_offer.objects.all()
    CategoryObj=Categories.objects.all()
    if request.method=="POST":
        discount=request.POST.get("discount")
        category=request.POST.get("category_name")
        discount=int(discount)
        if Category_offer.objects.filter(category=category).exists():
            print("already exists")
            messages.info(request,"Offer already exists for this Category")
            return redirect(CategoryOffer)
        if discount>0:
            if discount<90:
                newCategoryOffer=Category_offer()
                newCategoryOffer.discount=discount
                newCategoryOffer.category=Categories.objects.get(id=category)
                newCategoryOffer.save()
                return redirect(CategoryOffer)
            else:
                messages.error(request,"Discount must be less than 90%")
                return redirect(CategoryOffer)
        else:
                messages.error(request,"Discount must be greater than 0%")
                return redirect(CategoryOffer)
    return render(request,'AdminPanel/categoryoffer.html',{'Category':CategoryObj,'offers':offers})

# ---------------------------- Edit CategoryOffer ---------------------------- #

def Edit_CategoryOffer(request,id):
    CategoryObj=Categories.objects.all()
    CategoryOfferObj=Category_offer.objects.get(id=id)
    if request.method=="POST":
        discount=request.POST.get("discount")
        category=request.POST.get("category_name")
        discount=int(discount)
        if discount>0:
            if discount<90:
                CategoryOfferObj.discount=discount
                CategoryOfferObj.category=Categories.objects.get(id=category)
                CategoryOfferObj.save()
                return redirect(CategoryOffer)
            else:
                messages.error(request,"Discount must be less than 90%")
                return redirect(Edit_CategoryOffer)
        else:
                messages.error(request,"Discount must be greater than 0%")
                return redirect(Edit_CategoryOffer)
    context={
        'Category':CategoryObj,
        'CategoryOffer':CategoryOfferObj
    }
    return render(request,'Offers/Edit_CategoryOffer.html',context)



# --------------------------- View category Offers --------------------------- #
# def View_CategoryOffers(request):
#     CategoryOfferObj=Category_offer.objects.all()
#     paginator=Paginator(CategoryOfferObj,per_page=2)
#     page_number=request.GET.get('page')
#     CategoryOfferObjfinal=paginator.get_page(page_number)
#     totalpage=CategoryOfferObjfinal.paginator.num_pages
#     context={
#         'CategoryOffer':CategoryOfferObjfinal,
#         'lastpage':totalpage,
#         'totalPagelist':[ n+1 for n  in range(totalpage)]

#     }
#     return render(request,'Offers/View_CategoryOffer.html',context)

# -------------------------- Delete A Category Offer ------------------------- #
def Delete_CategoryOffer(request,id):
    toDelete_CategoryOffer=Category_offer.objects.get(id=id)
    toDelete_CategoryOffer.delete()
    messages.success(request,'Offer Deleted successfully')
    return redirect(CategoryOffer)

# ---------------------------- Block CategoryOffer --------------------------- #
def Block_CategoryOffer(request,id):
    toBlock_CategoryOffer=Category_offer.objects.get(id=id)
    toBlock_CategoryOffer.is_active=False
    toBlock_CategoryOffer.save()
    messages.error(request, 'Offer is Blocked Successfully')
    return redirect(CategoryOffer)

# --------------------------- Unblock CategoryOffer -------------------------- #
def UnBlock_CategoryOffer(request,id):
    toUnBlock_CategoryOffer=Category_offer.objects.get(id=id)
    toUnBlock_CategoryOffer.is_active=True
    toUnBlock_CategoryOffer.save()
    messages.error(request, 'Offer is UnBlocked Successfully')
    return redirect(CategoryOffer)

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

def SubCategoryOffer(request):
    offers=SubCategory_offer.objects.all()
    SubcategObj=SubCategories.objects.all()
    if request.method=="POST":
        discount=request.POST.get("discount")
        category=request.POST.get("category_name")
        discount=int(discount)
        if SubCategory_offer.objects.filter(subcategory=category).exists():
            print("already exists")
            messages.info(request,"Offer already exists for this Category")
            return redirect(SubCategoryOffer)
        if discount>0:
            if discount<90:
                newCategoryOffer=SubCategory_offer()
                newCategoryOffer.discount=discount
                newCategoryOffer.subcategory=SubCategories.objects.get(id=category)
                newCategoryOffer.save()
                return redirect(SubCategoryOffer)
            else:
                messages.error(request,"Discount must be less than 90%")
                return redirect(SubCategoryOffer)
        else:
                messages.error(request,"Discount must be greater than 0%")
                return redirect(SubCategoryOffer)
    return render(request,'AdminPanel/subcategoryoffer.html',{'SubCategory':SubcategObj,'offers':offers})



def RoomOffer(request):
    offers=Room_offer.objects.all()
    RoomObj=Rooms.objects.all()
    if request.method=="POST":
        discount=request.POST.get("discount")
        name=request.POST.get("room_name")
        discount=int(discount)
        if Room_offer.objects.filter(room=name).exists():
            print("already exists")
            messages.info(request,"Offer already exists for this Category")
            return redirect(RoomOffer)
        if discount>0:
            if discount<90:
                newCategoryOffer=Room_offer()
                newCategoryOffer.discount=discount
                newCategoryOffer.room=Rooms.objects.get(id=name)
                newCategoryOffer.save()
                return redirect(RoomOffer)
            else:
                messages.error(request,"Discount must be less than 90%")
                return redirect(RoomOffer)
        else:
                messages.error(request,"Discount must be greater than 0%")
                return redirect(RoomOffer)
    return render(request,'AdminPanel/roomoffer.html',{'RoomObj':RoomObj,'offers':offers})





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
    if request.method=='POST':
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
    pendingbooking=HotelBookings.objects.filter(status='Pending')
    checkin=HotelBookings.objects.filter(status='Check-in')
    checkout=HotelBookings.objects.filter(status='Check-out')
    cancelled=HotelBookings.objects.filter(status='Cancelled')
    return render(request,'AdminPanel/Bookings.html',{'bookings':bookings,'pendingbooking':pendingbooking,'checkin':checkin,'checkout':checkout,
    'cancelled':cancelled})





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




# ------------------------------- Sales Report ------------------------------- #

def salesReport(request):
    bookingreport = PaymentClass.objects.filter(booked_room__is_booked = True).order_by('-id')
    context = {
            'bookingreport':bookingreport
            }

    return render(request,'AdminPanel/bookingreport.html',context)


def monthly_report(request,date):
    frmdate = date
    fm = [2022, frmdate, 1]
    todt = [2022,frmdate,28]
    bookingreport = PaymentClass.objects.filter(booked_room__created_at__gte = datetime.date(fm[0],fm[1],fm[2]),booked_room__created_at__lte=datetime.date(todt[0],todt[1],todt[2]),booked_room__is_booked =True).order_by("-id")
    if len(bookingreport)>0:
        context = {
            'bookingreport':bookingreport,
        }
        return render(request,'AdminPanel/bookingreport.html',context)
    else:
        messages.error(request,"No Bookings")
        return render(request,'AdminPanel/bookingreport.html')



def yearly_report(request,date):
    frmdate = date
    fm = [frmdate, 1, 1]
    todt = [frmdate,12,31]
    bookingreport = PaymentClass.objects.filter(booked_room__created_at__gte = datetime.date(fm[0],fm[1],fm[2]),booked_room__created_at__lte=datetime.date(todt[0],todt[1],todt[2]),booked_room__is_booked =True).order_by("-id")
    if len(bookingreport)>0:
        context = {
            'bookingreport':bookingreport,
        }
        return render(request,'AdminPanel/bookingreport.html',context)
    else:
        messages.error(request,"No Bookings")
        return render(request,'AdminPanel/bookingreport.html')

def date_range(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if len(fromdate)>0 and len(todate)> 0 :
            frm = fromdate.split("-")
            tod = todate.split("-")
            fm = [int(x) for x in frm]
            todt = [int(x) for x in tod]
            bookingreport = PaymentClass.objects.filter(booked_room__created_at__gte = datetime.date(fm[0],fm[1],fm[2]),booked_room__created_at__lte=datetime.date(todt[0],todt[1],todt[2]) ,booked_room__is_booked =True)
            context = {
                'bookingreport':bookingreport,
            }
            return render(request,'AdminPanel/bookingreport.html',context)
        else:
            bookingreport = PaymentClass.objects.all()
            context = {
                'bookingreport': bookingreport ,
             }
    return render (request,"AdminPanel/bookingreport.html",context)


  