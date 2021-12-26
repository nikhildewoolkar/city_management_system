from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=500)
    phoneno=models.CharField(max_length=500)
    area=models.CharField(max_length=500)
    wardno=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    taluka=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    utype=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    def __str__(self):  # __str__
        return (self.user.username)

class Newsletter(models.Model):
    email=models.CharField(max_length=200)

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    sub=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)

class Issue(models.Model):
    auther=models.CharField(max_length=500)
    phoneno=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    header=models.CharField(max_length=500)
    text=models.CharField(max_length=500)
    date=models.CharField(max_length=500)
    areaadmin=models.CharField(max_length=500)
    area=models.CharField(max_length=500)
    wardno=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    taluka=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    status=models.CharField(max_length=500)