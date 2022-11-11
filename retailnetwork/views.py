from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Indentrepreneur, Products
from .serializers import ProductsSerializer, IndentrepreneurSerializer, DetailIndentrepreneurSerializer, \
    DetailProductsIndentrepreneurSerializer
from django.db.models import Avg


class AllObjectIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        indentrepreneur = Indentrepreneur.objects.all()
        serializer = IndentrepreneurSerializer(indentrepreneur, many=True)
        return Response({'Indentrepreneur': serializer.data, })


class FilterIndentrepreneurListView(generics.ListAPIView):
    queryset = Indentrepreneur.objects.all()
    serializer_class = IndentrepreneurSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['idContacts__idAddress__country']


class StatisticsAvgIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # avg = Dealership.objects.raw(
        #     'SELECT * FROM DEALERSHIP_DEALERSHIP WHERE DEBT > (SELECT AVG(DEBT) FROM DEALERSHIP_DEALERSHIP)')
        avg = Indentrepreneur.objects.aggregate(Avg('debt'))
        indentrepreneur = Indentrepreneur.objects.filter(debt__gt=avg['debt__avg'])
        serializer = IndentrepreneurSerializer(indentrepreneur, many=True)
        return Response({'Statistics': serializer.data, })


class FilterProductsIndentrepreneurListView(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = ['id']


class CreateIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailIndentrepreneurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        indentrepreneur = Indentrepreneur.objects.filter(id=pk)
        serializer = DetailIndentrepreneurSerializer(indentrepreneur, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        net_instance = Indentrepreneur.objects.get(id=pk)
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
        serializer = DetailIndentrepreneurSerializer(instance=net_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        net_instance = Indentrepreneur.objects.get(id=pk)
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


class CreateProductIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        serializer = DetailProductsIndentrepreneurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateDeleteProductIndentrepreneurView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        product = Products.objects.filter(id=pk)
        serializer = DetailProductsIndentrepreneurSerializer(product, many=True)
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
            'idIndentrepreneur': request.data.get('idIndentrepreneur'),
        }
        serializer = DetailProductsIndentrepreneurSerializer(instance=net_instance, data=data, partial=True)
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
