from rest_framework import serializers
from .models import Dealership, Contacts, Products


class DetailDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealership
        fields = '__all__'


class DealershipSerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()
    idProvider = serializers.StringRelatedField()

    class Meta:
        model = Dealership
        fields = ['name', 'date_create', 'employees', 'idContacts', 'idContacts_id', 'idProvider', 'idProvider_id',
                  'debt']


class ProductsSerializer(serializers.ModelSerializer):
    idDealership = DealershipSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idDealership', 'idDealership_id']


class DetailProductsDealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
