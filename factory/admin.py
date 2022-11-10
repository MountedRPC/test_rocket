from django.contrib import admin
from .models import *


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ("name", "idContacts", "employees", "date_create",)
    list_filter = ("idContacts__idAddress__country",)
    search_fields = ("name__startswith",)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "date", "idFactory",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "idAddress",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street", "house",)
