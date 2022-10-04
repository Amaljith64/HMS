import imp
from django.shortcuts import render, redirect, HttpResponse
from AdminPanel.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from django.contrib import messages
from AdminPanel.views import category
from django.db.models import Q
from Payments.models import PaymentClass
from Payments.views import paymentfun
from .models import *
from .forms import *

from django.shortcuts import get_object_or_404
from Payments.models import *
from datetime import datetime


#----------------------ROOM  AND FILTER----------------------#


#                                   functions                                  #


def check_booking(start_date, end_date, id, room_count):
    print('Reached Checkinggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg')
    print(start_date)
    print(end_date)
    print(room_count)
    qs = HotelBookings.objects.filter(
        is_booked=True,
        start_date__lte=start_date,  # less than or equal
        end_date__gte=end_date,  # greater than or equal
        hotel__id=id
    )
    print(qs)
    if len(qs) >= room_count:
        return False
    return True


def check_availability(check_in, check_out):
    avail_list = []
    booking_list = HotelBookings.objects.filter(
        is_booked=True,
        start_date__lte=check_in,  # less than or equal
        end_date__gte=check_out)
    for booking in booking_list:
        if booking.hotel:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)


def find_total_room_charge(days, price):
    total = days * price
    return total


#----------------------------------function ends---------------------------------#


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


# def starAverage(id):
#     ratings=[]
#     onestar=ReviewRating.objects.filter(product=id,status=True,rating=1).count()
#     twostar=ReviewRating.objects.filter(product=id,status=True,rating=2).count()
#     threestar=ReviewRating.objects.filter(product=id,status=True,rating=3).count()
#     fourstar=ReviewRating.objects.filter(product=id,status=True,rating=4).count()
#     fivestar=ReviewRating.objects.filter(product=id,status=True,rating=5).count()

#     reviews = ReviewRating.objects.filter(product=id, status=True).aggregate(count=Count('id'))
#     count = 0
#     if reviews['count'] is not None:
#         count = int(reviews['count'])

#     onestarper=(onestar*count)/100
#     twostarper=(twostar*count)/100
#     threestarper=(threestar*count)/100
#     fourstarper=(fourstar*count)/100
#     fivestarper=(fivestar*count)/100
#     ratings.append[onestarper,twostarper,threestarper,fourstarper,fivestarper]
#     return all(ratings)






def hotel_detail(request, id):
    room = Rooms.objects.get(id=id)
    images = MultiImage.objects.filter(imageof=id)
    request.session['wallet'] = None
    request.session['amountfromwallet'] = 0
    scheckin = request.session['checkin']
    scheckout = request.session['checkout']

    if request.user.is_authenticated:
        try:
            orderproduct = HotelBookings.objects.filter(
                user=request.user, hotel=room).exists()
        except Rooms.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None
    if request.method == 'POST':
        if request.POST.get("form_type") == 'formOne':
            checkin = request.POST.get('checkin')
            checkout = request.POST.get('checkout')
            hotel = Rooms.objects.get(id=id)
            if checkin and checkout != "":
                if not check_booking(checkin, checkout, id, hotel.room_count):
                    messages.warning(
                        request, 'Hotel is already booked in these dates ')
                    print("already bookedddddddddddddddddddddd")
                    return redirect(hotel_detail, room.id)
                # try:
                value = HotelBookings.objects.create(
                    hotel=hotel, user=request.user, start_date=checkin, end_date=checkout)
                print(value.id)
                messages.success(request, 'Your booking has been saved')
                request.session['order_id'] = value.id
                print(checkin, 'ccccccccccccccccccccccccccccccccc')
                d1 = datetime.strptime(checkin, "%Y-%m-%d")
                d2 = datetime.strptime(checkout, "%Y-%m-%d")
                delta = d2 - d1
                print(delta.days, 'deltaaaaaaaaaaaaaaaaaaaaa')

                if room.discount_price > 0:
                    request.session['amount'] = find_total_room_charge(
                        delta.days, value.hotel.discount_price)
                    request.session['fullamount'] = find_total_room_charge(
                        delta.days, value.hotel.price)
                else:
                    request.session['amount'] = find_total_room_charge(
                        delta.days, value.hotel.price)

                request.session['original amount'] = request.session['amount']
                request.session['coupon'] = None

                return redirect(paymentfun, id=value.id)
                # except:
                #     messages.error(request, 'Please login to Book Your Room')

            else:
                messages.error(request, 'Please FIll all Fields')

        elif request.POST.get("form_type") == 'formTwo':
            print('fooooooorm2')
            try:

                reviews = ReviewRating.objects.get(
                    user__id=request.user.id, product__id=id)
                form = ReviewForm(request.POST, instance=reviews)
                form.save()
                messages.success(
                    request, 'Thank you! Your review has been updated.')
                return redirect(hotel_detail, id)
            except ReviewRating.DoesNotExist:
                print('exceptttttt')
                form = ReviewForm(request.POST)
                if form.is_valid():
                    data = ReviewRating()
                    data.subject = form.cleaned_data['subject']
                    data.rating = form.cleaned_data['rating']
                    data.review = form.cleaned_data['review']

                    data.product_id = id
                    data.user_id = request.user.id
                    data.save()
                    messages.success(
                        request, 'Thank you! Your review has been submitted.')
                    return redirect(hotel_detail, id)
    reviews = ReviewRating.objects.filter(product_id=room, status=True)
    # rating=starAverage(id)
    # print(rating,'ppppppppppppppppppp')

    return render(request, 'UserHome/viewroom.html', {'room': room,
                                                      'images': images,
                                                      'scheckin': scheckin,
                                                      'scheckout': scheckout,
                                                      'orderproduct': orderproduct,
                                                      'reviews': reviews})


def Bookings(request):
    user = request.user
    bookingdetails = HotelBookings.objects.filter(user=user)

    booking = PaymentClass.objects.filter(user=user)

    return render(request, 'UserHome/bookings.html', {'booking': booking})


def CancelBooking(request, id):
    print('cancelllllllllllllllll')
    user = request.user
    booking = PaymentClass.objects.filter(user=user)
    tocancel = PaymentClass.objects.get(id=id)
    print(tocancel.booked_room.id, 'hhooooooiiii')
    tocancelbooking = HotelBookings.objects.get(id=tocancel.booked_room.id)

    tocancelbooking.status = "Cancelled"
    print(tocancelbooking.status, 'rooooooommmmmmmmmmmmm')
    tocancelbooking.is_booked = False
    tocancelbooking.save()

    wallet_balance_add = MyWallet.objects.get(user=user)
    balance = wallet_balance_add.balance+float(tocancel.total_amount)
    wallet_balance_add.balance = balance
    wallet_balance_add.save()

    getwallet = WalletDetails.objects.create(user=user)
    getwallet.user = user
    getwallet.amount = tocancel.total_amount
    getwallet.decription_amount = "Booking Cancelled Amount"
    getwallet.status = "True"
    getwallet.save()
    messages.success(request, 'Amount Credited To Wallet')

    return redirect(Bookings)


#----------------------BOOKING AND MANAGEMENT ENDS-------------------#


#----------------------WISHLIST AND MANAGEMENT-------------------#


def add_to_wishlist(request, id):
    try:

        wish = get_object_or_404(Rooms, id=id)

        wished_room, created = Wishlist.objects.get_or_create(wished_room=wish,
                                                              user=request.user,
                                                              )

        messages.success(request, 'The item was added to your wishlist')
    except:
        messages.error(request, 'Please login')

    return redirect(room)


def wishlist(request):
    user = request.user
    list = Wishlist.objects.filter(user=user)

    return render(request, 'UserHome/wishlist.html', {'list': list})


def remove_from_wishlist(request, id):
    to_remove = Wishlist.objects.get(id=id)
    to_remove.delete()
    messages.warning(request, 'Item removed from Wishlist')
    return redirect(wishlist)

#----------------------WISHLIST AND MANAGEMENT ENDS-------------------#


#----------------------USER PROFILE-------------------#

def user_profile(request):
    myuser = request.user
    wallet = MyWallet.objects.get(user=myuser)
    walletdetail = WalletDetails.objects.filter(user=myuser)
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']

        myuser.username = username
        myuser.email = email
        myuser.phone_number = phone

        myuser.save()
        return redirect(user_profile)

    return render(request, 'UserHome/userprofile.html', {'user': myuser, 'wallet': wallet, 'walletdetail': walletdetail})


def submit_review(request, id):
    url = request.META.get('HTTP_REFERER')
    print(url, 'gggggggggggg')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(
                request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = id
                data.user_id = request.user.id
                data.save()
                messages.success(
                    request, 'Thank you! Your review has been submitted.')
                return redirect(hotel_detail, id)
