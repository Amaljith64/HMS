from django.db import models
from AdminPanel.models import *

from MyAdmin.models import Account

# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
    wished_room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    