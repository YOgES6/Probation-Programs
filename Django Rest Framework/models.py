from django.db import models
  
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    checkin = models.CharField(max_length=200)
    checkout = models.CharField(max_length=200)
