from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.genera_serializers import MeasureUnitSerializer, CategoryProductSerializer,IndicatorSerializer

class MeasureUnitListAPIView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class IndicatorListAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer

class CategoryProductUnitListAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer





