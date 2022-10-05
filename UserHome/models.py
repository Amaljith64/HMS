from django.db import models

from MyAdmin.models import Account

# Create your models here.



class logo(models.Model):
    img=models.ImageField(upload_to="media/",default=True)

