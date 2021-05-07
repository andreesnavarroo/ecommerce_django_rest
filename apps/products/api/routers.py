from rest_framework.routers import DefaultRouter
from apps.products.api.views.gerenal_views import *
from apps.products.api.views.product_viewset import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename = 'products')
router.register(r'measure-unit', MeasureUnitViewSet, basename = 'measure_unit')
router.register(r'category_products', CategoryProductViewSet, basename = 'category_products')
router.register(r'indicators', IndicatorViewSet, basename = 'indicators')

urlpatterns = router.urls
