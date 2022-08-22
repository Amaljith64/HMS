from django.db import models
from django.shortcuts import render,redirect


from AdminPanel.models import *



#Create your views here.


def paymentfun(request,id):
    booking=HotelBookings.objects.get(id=id)
    if request.method=='POST':
        methodofpayment=request.POST['q']
        changes=HotelBookings(hotel=booking.hotel,user=booking.user,
        start_date=booking.start_date,end_date=booking.end_date,
        status='Order Confirmed',payment_method=methodofpayment)
        changes.save()
        return redirect('bookings')





    return render(request,'UserHome/payment.html',{'booking':booking})