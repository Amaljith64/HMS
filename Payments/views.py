from http.client import HTTPResponse
from multiprocessing import context
from django.contrib import messages
from django.http import HttpResponse
from django.db import models
from django.shortcuts import render, redirect
from django.conf import settings
from AdminPanel.models import *
from .models import *
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
import razorpay
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.http import HttpResponse
from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.


def paymentfun(request, id):
    coupon = Coupons.objects.all()
    booking = HotelBookings.objects.get(id=id)
    request.session['booking']=booking.id
    fullamount = request.session['fullamount']
    roomamount = request.session['amount']
    discountamt = fullamount-roomamount
    razamt = roomamount*100
    wallet = MyWallet.objects.get(user=request.user)
    wallet_status=request.session['wallet']
    wallet_amount=request.session['amountfromwallet']

    # coupondis=discountamt-totalamount
    if request.method == "POST":
        client = razorpay.Client(
            auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.order.create(
            {'amount': razamt, 'currency': 'INR', 'payment_capture': '1'})
        print(payment)
    usedcoupon = request.session['coupon']
    razkey=settings.RAZOR_KEY_ID

    context = {'booking': booking,
               'totalamount': roomamount,
               'coupon': coupon,
               'usedcoupon': usedcoupon,
               'fullamount': fullamount,
               'discountamt': discountamt,
               'razamt': razamt,
               'wallet': wallet,
               'wallet_status':wallet_status,
               'wallet_amount':wallet_amount,
               'razkey':razkey}

    return render(request, 'UserHome/payment.html', context)


@csrf_exempt
def success(request):
    order_id = request.session['order_id']
    print(order_id)
    roomamount = request.session['amount']
    print(roomamount)
    wallet_status=request.session['wallet']
    if wallet_status != None:
        wallet_balance_add = MyWallet.objects.get(user=request.user)
        getwallet = WalletDetails.objects.create(user=request.user)
        walletamount = request.session['amountfromwallet']
        wallet_balance_add.balance -= walletamount
        wallet_balance_add.save()
        getwallet.decription_amount = "Debited"
        getwallet.status= False
        getwallet.amount = walletamount
        getwallet.save()


    order = get_object_or_404(HotelBookings, id=order_id)
    order.is_booked = True
    order.status = "Checkin Pending"
    order.save()
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
    wallet_status=request.session['wallet']
    if wallet_status != None:
        wallet_balance_add = MyWallet.objects.get(user=request.user)
        getwallet = WalletDetails.objects.create(user=request.user)
        walletamount = request.session['amountfromwallet']
        wallet_balance_add.balance -= walletamount
        wallet_balance_add.save()
        getwallet.decription_amount = "Debited"
        getwallet.status= False
        getwallet.amount = walletamount
        getwallet.save()

    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)
    order.is_booked = True
    order.status = "Checkin Pending"
    order.save()
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
    order.is_booked = True
    order.status = "Checkin Pending"
    order.save()
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
    id = request.session['booking']
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
    
    id = request.session['booking']
    coupon_discount = int(coupon_discount_.discount)
    print(coupon_discount)
    discount_price = request.session['amount']
    discount_price = amount
    request.session['amount'] = discount_price
    request.session['coupon'] = None
    messages.success(request, "Coupon Removed")
    return redirect(paymentfun, id)


def UseWallet(request):
    id = request.session['booking']
    if request.method == 'POST':
        wallet_balance_add = MyWallet.objects.get(user=request.user)

        alltotal = request.session['amount']
        print(alltotal, 'alltotal')

        if wallet_balance_add.balance >= alltotal:
            print(wallet_balance_add.balance, 'walletbalance...............')

            request.session['amountfromwallet'] = alltotal
            request.session['amount'] = 0
            request.session['wallet'] = 'used'

        else:
            alltotal -= wallet_balance_add.balance
            request.session['amount'] = alltotal
            request.session['amountfromwallet'] = wallet_balance_add.balance
            request.session['wallet'] = 'partiallyused'

    return redirect(paymentfun, id)


def remove_wallet(request):
    id = request.session['booking']

    alltotal = request.session['amount']
    wallet_amount = request.session['amountfromwallet']
    request.session['amount'] = alltotal+wallet_amount
    request.session['wallet'] = None

    return redirect(paymentfun, id)


def WalletPayment(request):
    wallet_balance_add = MyWallet.objects.get(user=request.user)
    getwallet = WalletDetails.objects.create(user=request.user)

    walletamount = request.session['amountfromwallet']
    order_id = request.session.get('order_id')
    order = get_object_or_404(HotelBookings, id=order_id)
    order.is_booked = True
    order.status = "Checkin Pending"
    order.save()
    payment_id_generated = str(
        int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')))
    methodofpayment = "Wallet Payment"
    status = "Booked"
    pay = PaymentClass(user=request.user, booked_room=order, payment_id=payment_id_generated,
                       payment_method=methodofpayment, total_amount=walletamount, status=status)
    pay.save()

    try:
        couponid = request.session['couponid']
        print(couponid, 'cccccccccccoooooooooouuuuuupppppppoonnnnnnnn')
        coupon_status = Couponstatus.objects.get(id=couponid)
        coupon_status.status = True
        coupon_status.save()
    except:
        pass

    walletamount = request.session['amountfromwallet']
    wallet_balance_add.balance -= walletamount
    print(wallet_balance_add.balance, 'afterwalletbalance...............')
    wallet_balance_add.save()
    getwallet.decription_amount = "debited"
    getwallet.amount = walletamount
    getwallet.status= False
    getwallet.save()

    return render(request, 'success.html')


def invoice(request,id):
    details=PaymentClass.objects.get(id=id)

    return render(request,'UserHome/invoice.html',{'details':details})


