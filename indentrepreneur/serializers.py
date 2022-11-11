from rest_framework import serializers
from .models import Indentrepreneur, Products


class DetailIndentrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indentrepreneur
        fields = '__all__'


class IndentrepreneurSerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()
    idProvider = serializers.StringRelatedField()

    class Meta:
        model = Indentrepreneur
        fields = ['id', 'name', 'date_create', 'employees', 'idContacts', 'idContacts_id', 'idProvider',
                  'idProvider_id',
                  'debt']


class ProductsSerializer(serializers.ModelSerializer):
    idIndentrepreneur = IndentrepreneurSerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idIndentrepreneur', 'idIndentrepreneur_id']


class DetailProductsIndentrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'
