from rest_framework import serializers
from factory.models import Factory, Products
from datetime import datetime, date


class CreateFactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class DetailFactorySerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        if len(value) > 50:
            raise serializers.ValidationError("This field must be limited to 50 characters.")
        return value

    class Meta:
        model = Factory
        fields = '__all__'


class FactorySerializer(serializers.ModelSerializer):
    idContacts = serializers.StringRelatedField()

    class Meta:
        model = Factory
        fields = ['id', 'name', 'date_create', 'employees', 'idContacts', 'idContacts_id', ]


class ProductsSerializer(serializers.ModelSerializer):
    idFactory = FactorySerializer(read_only=True)

    class Meta:
        model = Products
        fields = ['id', 'name', 'model', 'date', 'idFactory', 'idFactory_id']


class DetailProductsFactorySerializer(serializers.ModelSerializer):
    def validate_name(self, value):
        if len(value) > 25:
            raise serializers.ValidationError("This field must be limited to 25 characters.")
        return value

    def validate_date(self, value):
        if datetime(value.year, value.month, value.day, value.hour, value.minute, value.second) > datetime.now():
            raise serializers.ValidationError(
                "Incorrectness of the entered date of release of the product on the market.")
        return value

    class Meta:
        model = Products
        fields = '__all__'
