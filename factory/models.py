from datetime import datetime

from django.db import models


# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=70, blank=True)
    city = models.CharField(max_length=70, blank=True, null=True)
    street = models.CharField(max_length=70, blank=True, null=True)
    house = models.IntegerField(blank=True, null=True)

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


class Factory(models.Model):
    name = models.CharField(max_length=70, blank=True)
    idContacts = models.ForeignKey(Contacts, on_delete=models.CASCADE)
    employees = models.IntegerField(default=0, blank=True)
    date_create = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Products(models.Model):
    name = models.CharField(max_length=70, blank=True)
    model = models.CharField(max_length=70, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)  # auto_now_add=True,:(
    idFactory = models.ForeignKey(Factory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
