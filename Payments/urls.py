import imp
from django import views
from django.urls import path
from Payments import views


urlpatterns = [
    path('<int:id>',views.paymentfun,name='payment'),
    # path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('success',views.success,name='success'),
]
