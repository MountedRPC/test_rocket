from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Distributor, Products
from .serializers import DistributorSerializer, ProductsSerializer, DetailDistributorSerializer, \
    DetailProductsDistributorSerializer
from django.db.models import Avg


class AllObjectDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        distributor = Distributor.objects.all()
        serializer_dealership = DistributorSerializer(distributor, many=True)
        return Response({'Distributor': serializer_dealership.data, })


class FilterDistributorListView(generics.ListAPIView):
    queryset = Distributor.objects.all()
    serializer_class = DistributorSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['idContacts__idAddress__country']


class StatisticsAvgDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # avg = Dealership.objects.raw(
        #     'SELECT * FROM DEALERSHIP_DEALERSHIP WHERE DEBT > (SELECT AVG(DEBT) FROM DEALERSHIP_DEALERSHIP)')
        avg = Distributor.objects.aggregate(Avg('debt'))
        distributor = Distributor.objects.filter(debt__gt=avg['debt__avg'])
        serializer_dealership = DistributorSerializer(distributor, many=True)
        return Response({'Statistics': serializer_dealership.data, })


class FilterProductsDistributorListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailDistributorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        distributor = Distributor.objects.filter(id=pk)
        serializer = DetailDistributorSerializer(distributor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        net_instance = Distributor.objects.get(id=pk)
        if not net_instance:
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
        serializer = DetailDistributorSerializer(instance=net_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        net_instance = Distributor.objects.get(id=pk)
        if not net_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        net_instance.delete()
        return Response(
            {"message": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CreateProductDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailProductsDistributorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProductDistributorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        product = Products.objects.filter(id=pk)
        serializer = DetailProductsDistributorSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        net_instance = Products.objects.get(id=pk)
        if not net_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
            'model': request.data.get('model'),
            'date': request.data.get('date'),
            'idDistributor': request.data.get('idDistributor'),
        }
        serializer = DetailProductsDistributorSerializer(instance=net_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        net_instance = Products.objects.get(id=pk)
        if not net_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        net_instance.delete()
        return Response(
            {"message": "Object deleted!"},
            status=status.HTTP_200_OK
        )
