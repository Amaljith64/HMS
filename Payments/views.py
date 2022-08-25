from django.db import models
from django.shortcuts import render,redirect
from django.conf import settings
from AdminPanel.models import *
import razorpay
from django.views.decorators.csrf import csrf_exempt



#Create your views here.


def paymentfun(request,id):
    booking=HotelBookings.objects.get(id=id)
    roomamount=booking.hotel.price
    amount = int(roomamount) * 100
    client = razorpay.Client(auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))
    payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
    print(payment)
    if request.method=='POST':
        methodofpayment=request.POST['q']
        if methodofpayment=='RAZORPAY':    
            booking.payment_method=methodofpayment
            booking.save()
            return render(request, 'test.html', {'payment': payment})
        if methodofpayment=='PAY AT HOTEL':
            booking.payment_method=methodofpayment
            booking.status='Order Confirmed'
            booking.save()
            return redirect('userbookings')
    return render(request,'UserHome/payment.html',{'booking':booking,'payment': payment})



@csrf_exempt
def success(request):
    if request.method == "POST":
        a = request.POST
        order_id = ""
        for key, val in a.items():
            if key == 'razorpay_order_id':
                order_id = val
                break
        # user = Paisa.objects.filter(payment_id=order_id).first()
        # user.paid = True
        # user.save()
    return redirect('userbookings')




# @csrf_exempt
# def paymenthandler(request):
 
#     # only accept POST request.
#     if request.method == "POST":
#         try:
           
#             # get the required parameters from post request.
#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             signature = request.POST.get('razorpay_signature', '')
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
 
#             # verify the payment signature.
#             result = razorpay_client.utility.verify_payment_signature(
#                 params_dict)
#             if result is None:
#                 amount = 20000  # Rs. 200
#                 try:
 
#                     # capture the payemt
#                     razorpay_client.payment.capture(payment_id, amount)
 
#                     # render success page on successful caputre of payment
#                     return render(request, 'success.html')
#                 except:
 
#                     # if there is an error while capturing payment.
#                     return render(request, 'failed.html')
#             else:
 
#                 # if signature verification fails.
#                 return render(request, 'failed.html')
#         except:
 
#             # if we don't find the required parameters in POST data
#             return HttpResponseBadRequest()
#     else:
#        # if other than POST request is made.
#         return HttpResponseBadRequest()





