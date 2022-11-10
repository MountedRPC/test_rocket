from rest_framework import serializers
from factory.models import Factory, Contacts, Address


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['name', 'date_create', 'employees', 'idContacts_id__country', ]


class FactorySerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()

    class Meta:
        model = Factory
        fields = ['name', 'date_create', 'employees', 'idContacts', 'idContacts_id', ]
