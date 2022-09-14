from http.client import HTTPResponse
from django.contrib import messages
from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.conf import settings
from AdminPanel.models import *
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
    fullamount=request.session['fullamount']
    roomamount = request.session['amount']
    discountamt=fullamount-roomamount
    razamt=roomamount*100

    # coupondis=discountamt-totalamount

    user = request.user
    if request.method == "POST":
        client = razorpay.Client(
            auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))
        payment = client.order.create(
            {'amount':razamt, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
    usedcoupon = request.session['coupon']

    return render(request, 'UserHome/payment.html', {'booking': booking, 'totalamount': roomamount, 'coupon': coupon, 
    'usedcoupon': usedcoupon,'fullamount':fullamount,
    'discountamt':discountamt,'razamt':razamt})


@csrf_exempt
def success(request):
    order_id = request.session['order_id']
    print(order_id)
    roomamount = request.session['amount']
    print(roomamount)
    
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
    try:
        couponid = request.session['couponid']
        print(couponid, 'cccccccccccoooooooooouuuuuupppppppoonnnnnnnn')
        coupon_status = Couponstatus.objects.get(id=couponid)
        coupon_status.status = True
        coupon_status.save()
    except:
        pass
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

    try:
        couponid = request.session['couponid']
        print(couponid, 'cccccccccccoooooooooouuuuuupppppppoonnnnnnnn')
        coupon_status = Couponstatus.objects.get(id=couponid)
        coupon_status.status = True
        coupon_status.save()
    except:
        pass

    return render(request, 'success.html')


def apply_coupon(request):
    roomamount = request.session['amount']
    id = booking.id
    coupon = request.session['coupon']
    if request.method == "POST":
        if coupon == None:
            code = request.POST['code']
            if Coupons.objects.filter(coupon_code__icontains=code):
                if Coupons.objects.filter(coupon_code__icontains=code, active=True):
                    obj = Coupons.objects.get(coupon_code=code)
                    if roomamount > obj.min_amount and roomamount < obj.max_amount:
                        if Couponstatus.objects.filter(couponsid=obj.id, user=request.user, status=True):
                            print("coupon useddddddddddddddddddddddddddddddddddd")
                            messages.error(request, "Coupon Used")
                        else:
                            request.session['coupon'] = obj.coupon_code
                            discount = int(obj.discount)
                            print(obj.id)
                            c = Couponstatus()
                            c.user = request.user
                            c.couponsid = obj
                            c.save()
                            request.session['couponid'] = c.id
                            print(c.id, 'ccccccccccc.iddddd')
                            print(discount)
                            totalamount = roomamount-(roomamount*discount/100)
                            request.session['amount'] = totalamount
                            obj.save()
                            messages.success(request, "Coupon Applied")
                    else:
                        messages.error(request, "Price not in range")
                else:
                    messages.error(request, "Coupon Expired")
            else:
                messages.error(request, "Invalid Coupon")
        else:
            messages.error(request, "Coupon Already Applied")
    return redirect(paymentfun, id)


def remove_coupon(request):
    amount = request.session['original amount']
    to_remove = request.session['coupon']
    coupon_discount_ = Coupons.objects.get(coupon_code__icontains=to_remove)
    remove_ = Couponstatus.objects.filter(
        couponsid=coupon_discount_.id, user=request.user)
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
    messages.success(request, "Coupon Removed")
    return redirect(paymentfun, id)
