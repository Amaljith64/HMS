from django import views
from django.urls import path
from AdminPanel import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('viewroom',views.rooms,name='viewroom'),
    path('guest',views.guest,name='guest'),
    path('blockuser/<int:id>',views.blockuser,name='blockuser'),
    path('addroom',views.addrooms,name='addroom'),
    path('editroom/<int:id>',views.editroom,name='editroom'),
    path('delete/<int:id>',views.deleteroom,name='deleteroom'),
    path('category',views.category,name='category'),
    path('subcategory',views.subcategory,name='subcategory'),
]
