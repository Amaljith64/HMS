from http.client import HTTPResponse
from django.http import HttpResponse
from django.db import models
from django.shortcuts import render,redirect
from django.conf import settings
from AdminPanel.models import *
from decimal import Decimal
from .models import PaymentClass
from django.shortcuts import render, HttpResponse, redirect, \
    get_object_or_404, reverse
import razorpay
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import datetime
import json
from django.http import HttpResponse, JsonResponse
from paypal.standard.forms import PayPalPaymentsForm

#Create your views here.
# client = razorpay.Client(auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))



def paymentfun(request,id):
    global booking
    booking=HotelBookings.objects.get(id=id)
    global amount
    roomamount=booking.hotel.price
    amount = int(roomamount)

    user=request.user

    client = razorpay.Client(auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))
    global payment
    global payment_id
    payment = client.order.create({'amount': amount*100, 'currency': 'INR', 'payment_capture': '1'})
    payment_id=payment['id']
    print(payment)
    print("Ssssssssssssssssssssssssssssssssssssssssssssssssssssssssss")
    # pay = PaymentClass(user=user,payment_id=payment_id,payment_method=methodofpayment,total_amount=amount,status=status)
    # pay.save()
    return render(request, 'UserHome/payment.html', {'payment': payment,'booking':booking})
    


@csrf_exempt
def razorpaysuccess(request):
    user =request.user
    methodofpayment ="Razorpay"
    status = "success"
    pay = PaymentClass(user=user,payment_id=payment_id,payment_method=methodofpayment,total_amount=amount,status=status)
    pay.save()
    booking.payment_method="Razorpay"
    booking.status ="success"
    booking.save(update_fields=['payment_method','status'])
    return render(request,'success.html')

    # if request.method == "POST":
    #     a = request.POST
    #     order_id = ""
    #     for key, val in a.items():
    #         if key == 'razorpay_order_id':
    #             order_id = val
    #             break
    #     user = PaymentClass.objects.filter(payment_id=order_id).first()
    #     user.paid = True
    #     user.save()
    # return render(request, 'success.html')


# def paymentfun(request,id):
#     booking=HotelBookings.objects.get(id=id)
#     roomamount=booking.hotel.price
#     amount = int(roomamount)
#     currency = 'INR'

#     if request.method=='POST':
#         methodofpayment=request.POST['q']
#         if methodofpayment=='RAZORPAY':
            
#             razorpay_order = client.order.create(dict(amount=amount, currency=currency,payment_capture='1'))
#             razorpay_order_id=razorpay_order['id']
#             callback_url='success'
#             context = {}
#             context['razorpay_order_id'] = razorpay_order_id
#             context['razorpay_merchant_key'] = "rzp_test_EHJnISgTdTzYsc"
#             context['amount'] = amount 
#             context['currency'] = currency      
#             context['callback_url'] = callback_url
#             # context['payment']=payment
#             print(razorpay_order)   
#             # booking.payment_method=methodofpayment
#             # booking.status='Order Confirmed'
#             # booking.save()
#             return render(request, 'UserHome/payment.html', context=context)
#         if methodofpayment=='PAY AT HOTEL':
#             booking.payment_method=methodofpayment
#             # booking.status='Order Confirmed'
#             booking.save()
#         if methodofpayment=='PAYPAL':
#             booking.payment_method=methodofpayment
#             # booking.status='Order Confirmed'
#             booking.save()
#             return redirect(paypal)
#     return render(request,'UserHome/payment.html',{'booking':booking})




# @csrf_exempt
# def paymenthandler(request):
#     if request.method == "POST":
#         try:

#             payment_id = request.POST.get('razorpay_payment_id', '')
#             razorpay_order_id = request.POST.get('razorpay_order_id', '')
#             amount = request.POST.get('amount', '')
#             signature = request.POST.get('razorpay_signature', '')
#             print(payment_id)
#             print(razorpay_order_id)
#             print(signature)
#             params_dict = {
#                 'razorpay_order_id': razorpay_order_id,
#                 'razorpay_payment_id': payment_id,
#                 'razorpay_signature': signature
#             }
            
#             result = client.utility.verify_payment_signature(
#                 params_dict)
#             if result is None:
#                 print(amount)
#                 amount=amount
#                 try:
    
#                     # capture the payemt
#                     client.payment.capture(payment_id, amount)
    
#                     # render success page on successful caputre of payment
#                     return HttpResponse('success')
#                 except:
    
#                     # if there is an error while capturing payment.
#                     return HttpResponse('failed')
#             else:
    
#                     # if signature verification fails.
#                     return HttpResponse('payment failed')
#         except:
#             return HttpResponse('we didnt find the required parameters')
#     else:
#         return HttpResponse('not a post method')


def paypal(request):


    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': order.hotel.price,
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host,reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'UserHome/paypal.html', {'order': order, 'form': form})

@csrf_exempt
def payment_done(request):
    return HttpResponse("success")


@csrf_exempt
def payment_canceled(request):
    return HttpResponse("failed")


    # body = json.loads(request.body)
    # payment_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))) 
    # methodofpayment ="Paypal"
    # status ="paid"
    # pay = PaymentClass(user=request.user,payment_id=payment_id_generated,payment_method=methodofpayment,total_amount=amount,status=status)
    # pay.save()
    # booking.payment_method="Paypal"
    # booking.status ="paid"
    # booking.save(update_fields=['payment_method','status'])

    
    return render(request,'UserHome/paypal.html',{"pay":pay})
def payments(request):
        body = json.loads(request.body)
        pay = PaymentClass(
        
        user = request.user,
        payment_id = body['transID'],
        payment_method = body['payment_method'],
        amount =amount,
        )
        pay.save()
        data = {
        "orderID":pay.order_id,
        "transID":payments.payment_id,
        }

        return JsonResponse(data)
def order_complete(request):
    order_number    = request.GET.get("orderID")
    transID         = request.GET.get("transID")
    return render(request,'success.html')

def paymentsuccess(request):

    payment_id_generated = str(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))) 
    methodofpayment ="Pay At Hotel"
    status ="booked"
    pay = PaymentClass(user=request.user,payment_id=payment_id_generated,payment_method=methodofpayment,total_amount=amount,status=status)
    pay.save()
    booking.payment_method="Pay At Hotel"
    booking.status ="booked"
    booking.save(update_fields=['payment_method','status'])


    return render(request,'success.html')
