from http.client import HTTPResponse
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
from datetime import date
import datetime
import json
from django.http import HttpResponse, JsonResponse
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.


def paymentfun(request, id):
    global booking
    booking = HotelBookings.objects.get(id=id)
    global amount
    roomamount = booking.hotel.price
    amount = int(roomamount)

    user = request.user
    if request.method == "POST":
        client = razorpay.Client(
            auth=("rzp_test_EHJnISgTdTzYsc", "FPEocjz0VBuibVylwibhSwpX"))
        payment = client.order.create(
            {'amount': amount, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)

    return render(request, 'UserHome/payment.html', {'booking': booking})


@csrf_exempt
def success(request):
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
    return HttpResponse("success")


@csrf_exempt
def payment_canceled(request):
    return HttpResponse("failed")


def paymentsuccess(request):

    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Pay At Hotel"
    status = "booked"
    pay = PaymentClass(user=request.user, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=amount, status=status)
    pay.save()
    booking.payment_method = "Pay At Hotel"
    booking.status = "booked"
    booking.save(update_fields=['payment_method', 'status'])

    return render(request, 'success.html')
