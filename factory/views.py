from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from factory.models import Factory, Products
from factory.serializers import FactorySerializer, ProductsSerializer, DetailFactorySerializer, \
    DetailProductsFactorySerializer


class AllObjectFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        factory = Factory.objects.all()
        serializer_factory = FactorySerializer(factory, many=True)
        return Response({'Factory': serializer_factory.data, })


class FilterFactoryListView(generics.ListAPIView):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['idContacts__idAddress__country']


class FilterProductsFactoryListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailFactorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        factory = Factory.objects.filter(id=pk)
        serializer = DetailFactorySerializer(factory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        factory_instance = Factory.objects.get(id=pk)
        if not factory_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'idContacts': request.data.get('idContacts'),
            'employees': request.data.get('employees'),
            'idProvider': request.data.get('idProvider'),
        }
        serializer = DetailFactorySerializer(instance=factory_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        factory_instance = Factory.objects.get(id=pk)
        if not factory_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        factory_instance.delete()
        return Response(
            {"message": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CreateProductFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailProductsFactorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProductFactoryView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        product = Products.objects.filter(id=pk)
        serializer = DetailProductsFactorySerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        product_instance = Products.objects.get(id=pk)
        if not product_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'model': request.data.get('model'),
            'date': request.data.get('date'),
            'idFactory': request.data.get('idFactory'),
        }
        serializer = DetailProductsFactorySerializer(instance=product_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        product_instance = Products.objects.get(id=pk)
        if not product_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        product_instance.delete()
        return Response(
            {"message": "Object deleted!"},
            status=status.HTTP_200_OK
        )
