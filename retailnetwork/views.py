from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Retailnetwork, Products
from .serializers import ProductsSerializer, RetailnetworkSerializer, DetailRetailnetworkSerializer, \
    DetailProductsRetailnetworkSerializer
from django.db.models import Avg


class AllObjectRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        retailnetwork = Retailnetwork.objects.all()
        serializer = RetailnetworkSerializer(retailnetwork, many=True)
        return Response({'Retailnetwork': serializer.data, })


class FilterRetailnetworkListView(generics.ListAPIView):
    queryset = Retailnetwork.objects.all()
    serializer_class = RetailnetworkSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['idContacts__idAddress__country']


class StatisticsAvgRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # avg = Dealership.objects.raw(
        #     'SELECT * FROM Retailnetwork_Retailnetwork WHERE DEBT > (SELECT AVG(DEBT) FROM DEALERSHIP_DEALERSHIP)')
        avg = Retailnetwork.objects.aggregate(Avg('debt'))
        retailnetwork = Retailnetwork.objects.filter(debt__gt=avg['debt__avg'])
        serializer = RetailnetworkSerializer(retailnetwork, many=True)
        return Response({'Statistics': serializer.data, })


class FilterProductsRetailnetworkListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailRetailnetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        retailnetwork = Retailnetwork.objects.filter(id=pk)
        serializer = DetailRetailnetworkSerializer(retailnetwork, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        net_instance = Retailnetwork.objects.get(id=pk)
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
        serializer = DetailRetailnetworkSerializer(instance=net_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        net_instance = Retailnetwork.objects.get(id=pk)
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


class CreateProductRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailProductsRetailnetworkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProductRetailnetworkView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        product = Products.objects.filter(id=pk)
        serializer = DetailProductsRetailnetworkSerializer(product, many=True)
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
            'idRetailnetwork': request.data.get('idRetailnetwork'),
        }
        serializer = DetailProductsRetailnetworkSerializer(instance=net_instance, data=data, partial=True)
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
