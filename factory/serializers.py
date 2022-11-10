from rest_framework import serializers
from factory.models import Factory, Products


class DetailFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()

    class Meta:
        model = Factory
        fields = ['name', 'date_create', 'employees', 'idContacts', 'idContacts_id', ]


class ProductsSerializer(serializers.ModelSerializer):
    idFactory = FactorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idFactory', 'idFactory_id']


class DetailProductsFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
