from django.contrib import admin
from django.utils.html import format_html
from .models import *
from django.urls import reverse
from django.utils.http import urlencode


@admin.action(description='Mark the selected dealer set zero debt')
def set_zero_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ("name", "idContacts", "employees", "view_provider_link", "debt", "date_create",)
    list_filter = ("idContacts__idAddress__country",)
    search_fields = ("name__startswith",)
    actions = [set_zero_debt]

    def view_provider_link(self, obj):
        url = (
                reverse("admin:factory_factory_changelist")
                + "?"
                + urlencode({"id": f"{obj.idProvider}"})
        )
        return format_html('<a href="{}">{}</a>', url, obj.idProvider)

    view_provider_link.short_description = "Provider"


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "date", "idDistributor",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "idAddress",)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("country", "city", "street", "house",)
