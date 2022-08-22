from django import views
from django.urls import path
from AccountSection import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('otp/<int:id>/',views.otpcode,name='otp'),
    path('test',views.test,name="test"),
]
