from django.urls import path

from apps.products.api.views.gerenal_views import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductUnitListAPIView
from apps.products.api.views.product_views import (
    ProductListApiView, ProductCreateAPIView, 
    ProductRetrieveAPIView,ProductDestroyAPIView,
    ProductUpdateAPIView,
)

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name = 'measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name = 'indicator'),
    path('category_product/', CategoryProductUnitListAPIView.as_view(), name = 'category_product'),
    path('product/list/', ProductListApiView.as_view(), name = 'product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name = 'product_create'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name = 'product_retrieve'),
    path('product/update/<int:pk>/',ProductUpdateAPIView.as_view(), name = 'product_update'),    
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name = 'product_destroy'),


]