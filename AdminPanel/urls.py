from django import views
from django.urls import path
from AdminPanel import views

urlpatterns = [
    path('addroom',views.addrooms,name='addroom'),
    path('viewrooms',views.rooms,name='viewroom'),
    
]
