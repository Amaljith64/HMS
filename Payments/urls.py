import imp
from django import views
from django.urls import path
from Payments import views


urlpatterns = [
    path('<int:id>',views.paymentfun,name='payment'),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('success/',views.razorpaysuccess,name='success/'),
    path('paypal',views.paypal,name='paypal'),
    path('payments',views.payments,name='payments'),
    path('order_complete',views.order_complete,name='order_complete'),
    path('paymentsuccess',views.paymentsuccess,name='paymentsuccess'),

    
]
