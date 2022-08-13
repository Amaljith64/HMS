
from django.db import models
from MyAdmin.models import *
import uuid

# Create your models here.


class UserOTP(models.Model):
    name=models.ForeignKey(Account,on_delete=models.CASCADE,related_name="profile")
    phone_number=models.CharField(max_length=15)
    otp=models.CharField(max_length=100,null=True,blank=True)
    uid=models.CharField(default=f'{uuid.uuid4}',max_length=200)

    def __str__(self):
        return str(self.name)
