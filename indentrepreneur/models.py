from datetime import datetime

from django.db import models
from retailnetwork.models import Retailnetwork


# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=70, null=True, blank=True)
    street = models.CharField(max_length=70, null=True, blank=True)
    house = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.country

    class Meta:
        ordering = ['country']


class Contacts(models.Model):
    email = models.EmailField()
    idAddress = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['email']


class Indentrepreneur(models.Model):
    name = models.CharField(max_length=70, blank=True)
    idContacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    employees = models.IntegerField(default=0, blank=True)
    idProvider = models.ForeignKey(Retailnetwork, on_delete=models.CASCADE)
    debt = models.FloatField(default=0, blank=True)
    date_create = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Products(models.Model):
    name = models.CharField(max_length=70, blank=True)
    model = models.CharField(max_length=70, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    idIndentrepreneur = models.ForeignKey(Indentrepreneur, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
