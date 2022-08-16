from django import views
from django.urls import path
from AccountSection import views

urlpatterns = [
    path('',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),

    # path('signup',views.usersignup),
    path('otp/<int:id>/',views.otpcode,name='otp'),
    path('test',views.siginwithotp,name="test"),
]
