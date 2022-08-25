from django.shortcuts import render, redirect
from AdminPanel.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from django.contrib import messages
from AdminPanel.views import category
from django.db.models import Q
from Payments.views import paymentfun
from .models import Wishlist
from django.shortcuts import get_object_or_404


#----------------------ROOM  AND FILTER----------------------#



def room(request):
    scategory_objs = SubCategories.objects.all()
    rooms = Rooms.objects.all()
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    scateg = request.GET.getlist('scateg')
    print(scateg)
    if sort_by == 'ASC':
        rooms = rooms.order_by('price')
    elif sort_by == 'DSC':
        rooms = rooms.order_by('-price')
    if search:
        rooms = rooms.filter(
            Q(name__icontains=search) |
            Q(Desc__icontains=search))

    if len(scateg):
        rooms = rooms.filter(subcateg__title__in=scateg).distinct()

    context = {'rooms': rooms, 'scategory_objs': scategory_objs}

    return render(request, 'UserHome/allrooms.html', context)


#----------------------ROOM  AND FILTER ENDS----------------------#



#----------------------BOOKING AND MANAGEMENT-------------------#


def check_booking(start_date, end_date, id, room_count):
    qs = HotelBookings.objects.filter(
        start_date__lte=start_date,  # less than or equal
        end_date__gte=end_date,  # greater than or equal
        hotel__id=id
    )
    if len(qs) >= room_count:
        return False
    return True


def hotel_detail(request, id):
    room = Rooms.objects.get(id=id)
    images=MultiImage.objects.filter(imageof=id)
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        hotel = Rooms.objects.get(id=id)
        if not check_booking(checkin, checkout, id, hotel.room_count):
            messages.warning(
                request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        value=HotelBookings.objects.create(hotel=hotel, user=request.user,
                                     start_date=checkin, end_date=checkout,
                                     status='Pending')
        print(value.id)
        messages.success(request, 'Your booking has been saved')
        
        return redirect(paymentfun,id=value.id)
    return render(request, 'UserHome/viewroom.html', {'room': room,'images':images})



def Bookings(request):
    user=request.user
    booking=HotelBookings.objects.filter(user=user)

    return render(request,'USerHome/bookings.html',{'booking':booking})


def CancelBooking(request,id):
    user=request.user
    booking=HotelBookings.objects.get(id=id)
       
    booking.status="Cancelled"
    booking.save()

    return redirect(Bookings)


#----------------------BOOKING AND MANAGEMENT ENDS-------------------#



#----------------------WISHLIST AND MANAGEMENT-------------------#




def add_to_wishlist(request,id):

    wish = get_object_or_404(Rooms,id=id)

    wished_room, created = Wishlist.objects.get_or_create(wished_room=wish,
                                                          user=request.user,
                                                          )

    messages.info(request, 'The item was added to your wishlist')
    return redirect(room)

def wishlist(request):
    user=request.user
    list=Wishlist.objects.filter(user=user)

    return render(request,'UserHome/wishlist.html',{'list':list})


def remove_from_wishlist(request,id):
    to_remove=Wishlist.objects.get(id=id)
    to_remove.delete()
    return redirect (wishlist)

#----------------------WISHLIST AND MANAGEMENT ENDS-------------------#

