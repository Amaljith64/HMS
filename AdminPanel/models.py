from django.db import models

from MyAdmin.models import Account


# Create your models here.


class Categories(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class SubCategories(models.Model):
    id=models.AutoField(primary_key=True)
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Rooms(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    categ=models.ForeignKey(Categories,on_delete=models.CASCADE,null=True)      
    subcateg=models.ForeignKey(SubCategories,on_delete=models.CASCADE,null=True)      
    Desc=models.TextField()
    price=models.IntegerField(null=True)
    img=models.ImageField(upload_to="media/",default=True)
    room_count = models.IntegerField(default=10)

    def __str__(self):
        return self.name

class MultiImage(models.Model):
    imageof=models.ForeignKey( Rooms,on_delete=models.CASCADE,related_name='multiimages')
    image = models.FileField(upload_to="multiimage/")




class HotelBookings(models.Model):
    hotel= models.ForeignKey(Rooms  , related_name="hotel_bookings" , on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Account, related_name="user_bookings" , on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    date =models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100,default="pending",null=True)
    payment_method = models.CharField(max_length=100, null=True)







