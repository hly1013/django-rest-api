from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    # -> Product.objects.get(pk='abc')

    def get_queryset(self):
        pass


product_detail_view = ProductDetailAPIView.as_view()
