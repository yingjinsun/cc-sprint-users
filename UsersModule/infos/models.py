import datetime
from django.utils import timezone

from django.db import models


class User(models.Model):

    userID = models.AutoField(primary_key=True)
    nameLast = models.CharField(max_length=50)
    nameFirst = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    userAddress = models.CharField(max_length=50)

    def __str__(self):
        return self.nameLast + " " + self.nameFirst


class Address(models.Model):
    addressID = models.AutoField(primary_key=True)
    addressNo = models.CharField(max_length=50)
    streetName1 = models.CharField(max_length=50)
    streetName2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    countryCode = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=50)
    userId_fk = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.addressNo + ", "  +self.streetName1 + ", " + self.streetName2 + ", " + self.city