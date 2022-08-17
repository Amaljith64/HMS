from django import views
from django.urls import path
from UserHome import views

urlpatterns = [
   
    path('',views.room,name='userroomview'),
    path('room/<int:id>',views.viewroom,name='roomdetails')
]
