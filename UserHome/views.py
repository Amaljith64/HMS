import imp
from django.shortcuts import render, redirect,HttpResponse
from AdminPanel.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from django.contrib import messages
from AdminPanel.views import category
from django.db.models import Q
from Payments.models import PaymentClass
from Payments.views import paymentfun
from .models import Wishlist
from django.shortcuts import get_object_or_404
from Payments.models import *



#----------------------ROOM  AND FILTER----------------------#



# def rooms(request):
#     rooms = Rooms.objects.all()
#     firstDayStr = None
#     lastDateStr = None


#     def chech_availability(fd, ed):
#         availableRooms = []
#         for room in rooms:
#             availList = []
#             bookingList = HotelBookings.objects.filter(roomNumber=room)
#             if room.statusStartDate == None:
#                 for booking in bookingList:
#                     if booking.startDate > ed.date() or booking.endDate < fd.date():
#                         availList.append(True)
#                     else:
#                         availList.append(False)
#                 if all(availList):
#                     availableRooms.append(room)
#             else:
#                 if room.statusStartDate > ed.date() or room.statusEndDate < fd.date():
#                     for booking in bookingList:
#                         if booking.startDate > ed.date() or booking.endDate < fd.date():
#                             availList.append(True)
#                         else:
#                             availList.append(False)
#                         if all(availList):
#                             availableRooms.append(room)

#         return availableRooms

#     if request.method == "POST":
#         if "dateFilter" in request.POST:
#             firstDayStr = request.POST.get("fd", "")
#             lastDateStr = request.POST.get("ld", "")
#             firstDay = datetime.strptime(firstDayStr, '%Y-%m-%d')
#             lastDate = datetime.strptime(lastDateStr, '%Y-%m-%d')
#             rooms = chech_availability(firstDay, lastDate)
#         if "filter" in request.POST:
#             if (request.POST.get("number") != ""):
#                 rooms = rooms.filter(
#                     number__contains=request.POST.get("number"))
#             if (request.POST.get("capacity") != ""):
#                 rooms = rooms.filter(
#                     capacity__gte=request.POST.get("capacity"))
#             if (request.POST.get("nob") != ""):
#                 rooms = rooms.filter(
#                     numberOfBeds__gte=request.POST.get("nob"))
#             if (request.POST.get("type") != ""):
#                 rooms = rooms.filter(
#                     roomType__contains=request.POST.get("type"))
#             if (request.POST.get("price") != ""):
#                 rooms = rooms.filter(
#                     price__lte=request.POST.get("price"))
#             context = {
#                 "role": role,
#                 "rooms": rooms,
#                 "number": request.POST.get("number"),
#                 "capacity": request.POST.get("capacity"),
#                 "nob": request.POST.get("nob"),
#                 "price": request.POST.get("price"),
#                 "type": request.POST.get("type")
#             }
#             return render(request, path + "rooms.html", context)



def room(request):




    scategory_objs = SubCategories.objects.all()
    # rooms = Rooms.objects.all()
    # sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    scateg = request.GET.getlist('scateg')
    category = request.GET.get('category')
    print(scateg)
    
    # if sort_by == 'ASC':
    #     rooms = rooms.order_by('price')
    # elif sort_by == 'DSC':
    #     rooms = rooms.order_by('-price')
   

    if category == None:
        rooms = Rooms.objects.all()
    else:
        rooms = Rooms.objects.filter(
            subcateg__title=category)
   
        
        

        
    if search:
        rooms = rooms.filter(
            Q(name__icontains=search) |
            Q(Desc__icontains=search))

    # if len(scateg):
    #     rooms = rooms.filter(subcateg__title__in=scateg).distinct()

    context = {'rooms': rooms, 'scategory_objs': scategory_objs}

    return render(request, 'UserHome/allrooms.html', context)


#----------------------ROOM  AND FILTER ENDS----------------------#








#----------------------BOOKING AND MANAGEMENT-------------------#

#                                   functions                                  #



def check_booking(start_date, end_date, id, room_count):
    print('Reached Checkinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
    print(start_date)
    print(end_date)
    print(room_count)
    qs = HotelBookings.objects.filter(
        start_date__lte=start_date,  # less than or equal
        end_date__gte=end_date,  # greater than or equal
        hotel__id=id
    )
    print(qs)
    if len(qs) >= room_count:
        return False
    return True



def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = HotelBookings.objects.filter(room=room)
    for booking in booking_list:
        if booking.start_date > check_out or booking.end_date < check_in:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)




def find_total_room_charge(check_in, check_out, price):
    days = check_out-check_in
    total = days * price
    return total


#----------------------------------function ends---------------------------------#



def hotel_detail(request, id):
    room = Rooms.objects.get(id=id)
    images=MultiImage.objects.filter(imageof=id)
    request.session['wallet']=None
    request.session['amountfromwallet']=0
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        hotel = Rooms.objects.get(id=id)
        if checkin and checkout != "":
            if not check_booking(checkin, checkout, id, hotel.room_count):
                messages.warning(
                    request, 'Hotel is already booked in these dates ')
                print("already bookedddddddddddddddddddddd")
                return redirect (hotel_detail,room.id)
            try:
                value=HotelBookings.objects.create(hotel=hotel, user=request.user,start_date=checkin, end_date=checkout)
                print(value.id)
                messages.success(request, 'Your booking has been saved')
                request.session['order_id'] = value.id
                frm = checkin.split("-")
                tod = checkout.split("-")
                fm = [int(x) for x in frm]
                todt = [int(x) for x in tod]
                print(fm[2])
                print(todt[2])
                if room.discount_price>0:
                    request.session['amount'] = find_total_room_charge(
                        fm[2], todt[2], value.hotel.discount_price)
                    request.session['fullamount'] = find_total_room_charge(
                        fm[2], todt[2], value.hotel.price)
                else:
                    request.session['amount'] = find_total_room_charge(
                            fm[2], todt[2], value.hotel.price)

                request.session['original amount']=request.session['amount']
                request.session['coupon']=None
                

                
                return redirect(paymentfun,id=value.id)
            except:
                messages.error(request, 'Please login to Book Your Room')

        else:
            messages.error(request, 'Please FIll all Fields')

            
    return render(request, 'UserHome/viewroom.html', {'room': room,'images':images})



def Bookings(request):
    user=request.user
    bookingdetails=HotelBookings.objects.filter(user=user)

    booking=PaymentClass.objects.filter(user=user)

    return render(request,'USerHome/bookings.html',{'booking':booking})


def CancelBooking(request,id):
    print('cancelllllllllllllllll')
    user=request.user
    booking=PaymentClass.objects.filter(user=user)
    tocancelbooking=PaymentClass.objects.get(id=id)
       
    tocancelbooking.booked_room.status="Cancelled"
    tocancelbooking.booked_room.is_booked=False
    tocancelbooking.save()

    wallet_balance_add=MyWallet.objects.get(user=user)
    balance=wallet_balance_add.balance+float(tocancelbooking.total_amount)
    wallet_balance_add.balance=balance
    wallet_balance_add.save()

    getwallet=WalletDetails.objects.create(user=user)
    getwallet.user=user
    getwallet.amount=tocancelbooking.total_amount
    getwallet.decription_amount="Booking Cancelled Amount"
    getwallet.save()
    messages.success(request, 'Amount Credited To Wallet')


    return redirect(Bookings)


#----------------------BOOKING AND MANAGEMENT ENDS-------------------#



#----------------------WISHLIST AND MANAGEMENT-------------------#




def add_to_wishlist(request,id):
    try:

        wish = get_object_or_404(Rooms,id=id)

        wished_room, created = Wishlist.objects.get_or_create(wished_room=wish,
                                                            user=request.user,
                                                            )

        messages.success(request, 'The item was added to your wishlist')
    except:
        messages.error(request, 'Please login')

    return redirect(room)

def wishlist(request):
    user=request.user
    list=Wishlist.objects.filter(user=user)

    return render(request,'UserHome/wishlist.html',{'list':list})


def remove_from_wishlist(request,id):
    to_remove=Wishlist.objects.get(id=id)
    to_remove.delete()
    messages.warning(request, 'Item removed from Wishlist')
    return redirect (wishlist)

#----------------------WISHLIST AND MANAGEMENT ENDS-------------------#




#----------------------USER PROFILE-------------------#

def user_profile(request):
    myuser=request.user
    wallet=MyWallet.objects.get(user=myuser)
    walletdetail=WalletDetails.objects.filter(user=myuser)
    if request.method=='POST':
        username=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']

        myuser.username=username
        myuser.email=email
        myuser.phone_number=phone

        myuser.save()
        return redirect(user_profile)
        
        
    return render(request,'UserHome/userprofile.html',{'user':myuser,'wallet':wallet,'walletdetail':walletdetail})


def check_room(request):
    if request.method=='POST':
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']





    


