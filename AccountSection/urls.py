from django import views
from django.urls import path
from AccountSection import views

urlpatterns = [
    path('',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    # path('signup',views.usersignup),
    path('otp/',views.otpcode,name='otp'),
]
