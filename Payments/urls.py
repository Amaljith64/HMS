import imp
from django import views
from django.urls import path
from Payments import views


urlpatterns = [
    path('<int:id>',views.paymentfun,name='payment'),
    path('success',views.success,name='success/'),
    path('paypal',views.paypal,name='paypal'),
    path('paymentsuccess',views.paymentsuccess,name='paymentsuccess'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('apply_coupon', views.apply_coupon, name='apply_coupon'),
    path('remove_coupon', views.remove_coupon, name='remove_coupon'),
    path('usewallet', views.UseWallet, name='UseWallet'),
    path('remove_wallet', views.remove_wallet, name='remove_wallet'),

    
]
