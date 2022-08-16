from django.db import models

# Create your models here.


class Roomtype(models.Model):
    type=models.CharField(max_length=150,unique=True)
    def __str__(self):
        return self.type




class Rooms(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    # Location=models.ForeignKey(Location,on_delete=models.CASCADE,null=True)      
    Roomtype=models.ForeignKey(Roomtype,on_delete=models.CASCADE,null=True)      
    Desc=models.TextField()
    price=models.FloatField(null=True)
    img=models.ImageField(upload_to="media/",default=True)

    def __str__(self):
        return self.name



