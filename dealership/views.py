from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dealership, Products
from .serializers import DealershipSerializer, ProductsSerializer, DetailDealershipSerializer, \
    DetailProductsDealershipSerializer
from django.db.models import Avg


class AllObjectDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        dealership = Dealership.objects.all()
        serializer_dealership = DealershipSerializer(dealership, many=True)
        return Response({'Dealership': serializer_dealership.data, })


class FilterDealershipListView(generics.ListAPIView):
    queryset = Dealership.objects.all()
    serializer_class = DealershipSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['idContacts__idAddress__country']


class StatisticsAvgDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # avg = Dealership.objects.raw(
        #     'SELECT * FROM DEALERSHIP_DEALERSHIP WHERE DEBT > (SELECT AVG(DEBT) FROM DEALERSHIP_DEALERSHIP)')
        avg = Dealership.objects.aggregate(Avg('debt'))
        dealership = Dealership.objects.filter(debt__gt=avg['debt__avg'])
        serializer_dealership = DealershipSerializer(dealership, many=True)
        return Response({'Statistics': serializer_dealership.data, })


class FilterProductsDealershipListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailDealershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        dealership = Dealership.objects.filter(id=pk)
        serializer = DetailDealershipSerializer(dealership, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        dealership_instance = Dealership.objects.get(id=pk)
        if not dealership_instance:
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
        serializer = DetailDealershipSerializer(instance=dealership_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        dealership_instance = Dealership.objects.get(id=pk)
        if not dealership_instance:
            return Response(
                {"message": "Object with todo id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        dealership_instance.delete()
        return Response(
            {"message": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CreateProductDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailProductsDealershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProductDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        product = Products.objects.filter(id=pk)
        serializer = DetailProductsDealershipSerializer(product, many=True)
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
            'idDealership': request.data.get('idDealership'),
        }
        serializer = DetailProductsDealershipSerializer(instance=product_instance, data=data, partial=True)
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
