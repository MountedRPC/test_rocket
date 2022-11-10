from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from factory.models import Factory
from factory.serializers import FactorySerializer


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

# class StatisticsAvg
