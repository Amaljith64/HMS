from django.shortcuts import render
from AdminPanel.models import *
from django.http import HttpResponseRedirect, JsonResponse
# Create your views here.
from django.contrib import messages
from AdminPanel.views import category
from django.db.models import Q



def room(request):
    scategory_objs=SubCategories.objects.all()
    rooms=Rooms.objects.all()  
    sort_by = request.GET.get('sort_by')
    search = request.GET.get('search')
    scateg = request.GET.getlist('scateg')
    print(scateg)
    if sort_by == 'ASC':
        rooms=rooms.order_by('price')
    elif sort_by == 'DSC':
        rooms=rooms.order_by('-price')
    if search:
        rooms = rooms.filter(
            Q(name__icontains = search) |
            Q(Desc__icontains = search) )

    if len(scateg):
        rooms=rooms.filter(subcateg__title__in=scateg).distinct()

    context={'rooms':rooms,'scategory_objs':scategory_objs}

    return render(request,'UserHome/allrooms.html',context)




def check_booking(start_date  , end_date ,id , room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date,
        end_date__gte=end_date,
        hotel__id = id
        )
    if len(qs) >= room_count:
        return False   
    return True



def hotel_detail(request,id):
    room=Rooms.objects.get(id=id)
    if request.method == 'POST':
        checkin = request.POST.get('checkin')
        checkout= request.POST.get('checkout')
        hotel = Rooms.objects.get(id = id)
        if not check_booking(checkin ,checkout  , id , hotel.room_count):
            messages.warning(request, 'Hotel is already booked in these dates ')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        HotelBooking.objects.create(hotel=hotel , user = request.user , start_date=checkin
        , end_date = checkout , booking_type  = 'Pre Paid')     
        messages.success(request, 'Your booking has been saved')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))      
    return render(request , 'UserHome/viewroom.html' ,{'room':room})