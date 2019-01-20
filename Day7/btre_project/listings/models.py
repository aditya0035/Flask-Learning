from django.db import models
from datetime import datetime
from  realtors.models import Realtor
# Create your models here.

class Listing(models.Model):
    realtors=models.ForeignKey(Realtor,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipCode=models.CharField(max_length=20)
    description=models.TextField()
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    photo=models.ImageField(upload_to='photos/%y%m%d')
    list_date=models.DateTimeField(default=datetime.now)
    
    def __str__(self):
        return f'Owner : {self.realtors.name}  PropertyName : {self.title}'