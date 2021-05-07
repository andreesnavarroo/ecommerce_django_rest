from rest_framework import viewsets

from apps.products.models import MeasureUnit
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.genera_serializers import MeasureUnitSerializer, CategoryProductSerializer,IndicatorSerializer

class MeasureUnitViewSet(viewsets.GenericViewSet):
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)
    
    def create(self,request):
        return Response({})

class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self,request):
        data = self.get_queryset()
        data = self.get_serializer(data,many = True)
        return Response(data.data)

class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer




