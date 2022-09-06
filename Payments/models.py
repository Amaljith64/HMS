from django.db import models
from AdminPanel.models import HotelBookings
from MyAdmin.models import *


# Create your models here.


# class Payment(models.Model):
#     user = models.ForeignKey(Account, on_delete=models.CASCADE)
#     payment_id = models.CharField(max_length=100)
#     payment_method = models.CharField(max_length=100)
#     amount = models.CharField(max_length=100) # this is the total amount paid
#     status = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.payment_id
class PaymentClass(models.Model):
    booked_room=models.ForeignKey(HotelBookings,on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100) # this is the total amount paid
    status = models.CharField(max_length=100,default="pending")

    def __str__(self):
        return self.payment_id