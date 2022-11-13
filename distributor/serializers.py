from rest_framework import serializers
from .models import Distributor, Products


class DetailDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Distributor
        fields = '__all__'


class DistributorSerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()
    idProvider = serializers.StringRelatedField()

    class Meta:
        model = Distributor
        fields = ['id', 'name', 'date_create', 'employees', 'idContacts', 'idContacts_id', 'idProvider',
                  'idProvider_id',
                  'debt']


class ProductsSerializer(serializers.ModelSerializer):
    idDistributor = DistributorSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idDistributor', 'idDistributor_id']


class DetailProductsDistributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
