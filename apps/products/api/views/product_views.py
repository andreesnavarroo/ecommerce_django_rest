from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer
