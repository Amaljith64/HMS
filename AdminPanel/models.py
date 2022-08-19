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
    price=models.FloatField(null=True)
    img=models.ImageField(upload_to="media/",default=True)
    room_count = models.IntegerField(default=10)

    def __str__(self):
        return self.name


class HotelBooking(models.Model):
    hotel= models.ForeignKey(Rooms  , related_name="hotel_bookings" , on_delete=models.CASCADE)
    user = models.ForeignKey(Account, related_name="user_bookings" , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type= models.CharField(max_length=100,choices=(('Pre Paid' , 'Pre Paid') , ('Post Paid' , 'Post Paid')))




