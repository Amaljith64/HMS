from http.client import HTTPResponse
from django.contrib import messages
from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.conf import settings
from AdminPanel.models import *
from decimal import Decimal
from .models import PaymentClass
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
import razorpay
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import HttpResponse
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.


def paymentfun(request, id):
    coupon = Coupons.objects.all()
    global booking
    booking = HotelBookings.objects.get(id=id)

     
    roomamount = request.session['amount']
    
    

    user = request.user
    if request.method == "POST":
        client = razorpay.Client(
            auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))
        payment = client.order.create(
            {'amount': roomamount*100, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
    usedcoupon = request.session['coupon']

    return render(request, 'UserHome/payment.html', {'booking': booking, 'totalamount': roomamount, 'coupon': coupon, 'usedcoupon': usedcoupon})


@csrf_exempt
def success(request):
    order_id = request.session.get('order_id')
    roomamount = request.session['amount']
    
    order = get_object_or_404(HotelBookings, id=order_id)
    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Razorpay"
    status = "Transaction Completed"
    pay = PaymentClass(user=request.user, booked_room=order, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=roomamount, status=status)
    pay.save()

    return render(request, "success.html")


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
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment_cancelled')),
    }
    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'UserHome/paypal.html', {'order': order, 'form': form})


@csrf_exempt
def payment_done(request):
    roomamount = request.session['amount']
    
    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)
    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Paypal"
    status = "Transaction Completed"
    pay = PaymentClass(user=request.user, booked_room=order, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=roomamount, status=status)
    pay.save()

    return render(request, 'success.html')


@csrf_exempt
def payment_canceled(request):
    roomamount = request.session['amount']
   

    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)
    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Paypal"
    status = "Transaction Cancelled"
    pay = PaymentClass(user=request.user, booked_room=order, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=roomamount, status=status)
    pay.save()

    return render(request, 'failed.html')


def paymentsuccess(request):
    roomamount = request.session['amount']
    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)

    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Pay At Hotel"
    status = "Booked"
    pay = PaymentClass(user=request.user, booked_room=order, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=roomamount, status=status)
    pay.save()

    return render(request, 'success.html')


def apply_coupon(request):
    roomamount = request.session['amount']
    print(booking.id, "ooooooooooooooooooooooooooooooooooooooo")
    id = booking.id
    if request.method == "POST":
        code = request.POST['code']
        if Coupons.objects.filter(coupon_code__icontains=code, active=True):
            obj = Coupons.objects.get(coupon_code=code)
            if Couponstatus.objects.filter(couponsid=obj.id, user=request.user):
                print("coupon useddddddddddddddddddddddddddddddddddd")
                messages.error(request, "Coupon Unavailable")
            else:
                request.session['coupon'] = obj.coupon_code
                discount = int(obj.discount)
                print(obj.id)
                c = Couponstatus()
                c.user=request.user
                c.couponsid = obj
                c.save()

                print(discount)

                totalamount = roomamount-(roomamount*discount/100)
                request.session['amount'] = totalamount
                obj.save()
        else:
            messages.error(request, "Invalid Coupon")
    return redirect(paymentfun, id)


def remove_coupon(request):
    amount=request.session['original amount']
    to_remove = request.session['coupon']
    coupon_discount_ = Coupons.objects.get(coupon_code__icontains=to_remove)
    remove_=Couponstatus.objects.get(couponsid=coupon_discount_.id, user=request.user)
    remove_.delete()
    print('deleteddddddddd')
    print(booking.id)
    id = booking.id
    coupon_discount = int(coupon_discount_.discount)
    print(coupon_discount)
    discount_price = request.session['amount']
    discount_price = amount
    request.session['amount'] = discount_price
    request.session['coupon'] = None
    return redirect(paymentfun, id)
