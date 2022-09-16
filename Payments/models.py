from django.db import models
from AdminPanel.models import HotelBookings
from MyAdmin.models import *


# Create your models here.



class PaymentClass(models.Model):
    booked_room=models.ForeignKey(HotelBookings,on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=100)
    total_amount = models.CharField(max_length=100) # this is the total amount paid
    status = models.CharField(max_length=100,default="pending")

    def __str__(self):
        return self.payment_id


class Wallet(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    amount=models.FloatField( max_length=15, null = True, default= 0 )
    decription_amount=models.CharField(null=True,max_length=200)
    
    def _str_(self):
        return self.user.username

class WalletDetails(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    balance = models.FloatField(max_length=15, null = True, default= 0 )
    wallet=models.ForeignKey(Wallet,null=True,on_delete=models.CASCADE)