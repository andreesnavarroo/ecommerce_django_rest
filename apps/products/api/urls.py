from django.urls import path

from apps.products.api.views.gerenal_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductUnitListAPIView
from apps.products.api.views.product_views import ProductListApiView

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_product/', CategoryProductUnitListAPIView.as_view(), name = 'category_product'),
    path('product/', ProductListApiView.as_view(), name = 'product'),

]