from django import views
from django.urls import path
from UserHome import views

urlpatterns = [
   
    path('',views.room,name='userroomview'),
    path('check_booking/' , views.check_booking),
    path('room/<int:id>',views.hotel_detail ,name='roomdetails'),
    path('addwishlist/<int:id>',views.add_to_wishlist,name='addwishlist'),
    path('deletewish/<int:id>',views.remove_from_wishlist,name='delwishlist'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('userbookings',views.Bookings,name='userbookings'),
    path('cancelbooking/<int:id>',views.CancelBooking,name='CancelBooking'),
    path('profile',views.user_profile,name='profile'),
    path('submit_review/<int:id>',views.submit_review,name='submit_review'),
        # Generating Invoice
    path('generateinvoice/<int:id>/', views.GenerateInvoice.as_view(), name = 'generateinvoice'),

]
