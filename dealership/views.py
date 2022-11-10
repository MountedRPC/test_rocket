from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Dealership, Products
from .serializers import DealershipSerializer, ProductsSerializer, CreateDealershipSerializer
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
        return Response({'Dealership': serializer_dealership.data, })


class FilterProductsDealershipListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateDealershipView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = CreateDealershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
