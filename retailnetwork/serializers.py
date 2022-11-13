from rest_framework import serializers
from .models import Retailnetwork, Products


class DetailRetailnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailnetwork
        fields = '__all__'


class RetailnetworkSerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()
    idProvider = serializers.StringRelatedField()

    class Meta:
        model = Retailnetwork
        fields = ['id','name', 'date_create', 'employees', 'idContacts', 'idContacts_id', 'idProvider', 'idProvider_id',
                  'debt']


class ProductsSerializer(serializers.ModelSerializer):
    idRetailnetwork = RetailnetworkSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idRetailnetwork', 'idRetailnetwork_id']


class DetailProductsRetailnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
