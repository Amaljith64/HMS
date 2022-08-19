from django import views
from django.urls import path
from UserHome import views

urlpatterns = [
   
    path('',views.room,name='userroomview'),
    path('check_booking/' , views.check_booking),
    path('room/<int:id>',views.hotel_detail ,name='roomdetails')
]
