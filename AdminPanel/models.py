
from itertools import product
from django.db import models

from MyAdmin.models import Account
from UserHome.models import *
from django.db.models import Avg, Count


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
    discount_price=models.IntegerField(null=True)
    discount_percentage=models.IntegerField(null=True)

    def __str__(self):
        return self.name
       
    def reduced_price(self):
        return self.price - self.discount_price

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

    
        
        




class ReviewRating(models.Model):
    product = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Wishlist(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
    wished_room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
   

class Category_offer(models.Model):
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    discount=models.IntegerField()
    is_active = models.BooleanField(default=True)

class SubCategory_offer(models.Model):
    subcategory=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    discount=models.IntegerField()
    is_active = models.BooleanField(default=True)

class Room_offer(models.Model):
    room=models.ForeignKey(Rooms,on_delete=models.CASCADE)
    discount=models.IntegerField()
    is_active = models.BooleanField(default=True)



class MultiImage(models.Model):
    imageof=models.ForeignKey( Rooms,on_delete=models.CASCADE,related_name='multiimages')
    image = models.FileField(upload_to="multiimage/")




class HotelBookings(models.Model):
    hotel= models.ForeignKey(Rooms  , related_name="hotel_bookings" , on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(Account, related_name="user_bookings" , on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    is_booked=models.BooleanField(default=False)
    created_at =models.DateField(auto_now_add=True)
    status=models.CharField(max_length=50,default="Pending")



class Coupons(models.Model):
    coupon_code=models.CharField(max_length=100)
    description=models.CharField(max_length=100,null=True)
    valid_from=models.DateField(auto_now=True)
    valid_to=models.DateField(null=True)
    min_amount=models.IntegerField(null=True)
    max_amount=models.IntegerField(null=True)
    discount=models.IntegerField(null=True)
    active=models.BooleanField(default=True)


class Couponstatus(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    couponsid=models.ForeignKey(Coupons,on_delete=models.CASCADE,null=True)
    status=models.BooleanField(default=False)
 







