from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.products.models import Product
from apps.products.serializer import ProductCreateSerializer, ProductUpdateSerializer, ProductPartialUpdateSerializer


class ProductCreateAPIView(APIView):
    serializer_class = ProductCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailAPIView(APIView):
    # def get(self, request ,pk,*args,**kwargs):
    #     try:
    #         product = Product.objects.get(id=pk, is_active=True)
    #     except Product.DoesNotExist:
    #         return Response(data={"detail":"Product not found"}, status=status.HTTP_404_NOT_FOUND)
    pass


class ProductUpdateAPIView(APIView):
    @staticmethod
    def put(request, pk):
        try:
            product = Product.objects.get(pk=pk, is_active=True)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductUpdateSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductPartialUpdateAPIView(APIView):
    @staticmethod
    def patch(request, pk):
        try:
            product = Product.objects.get(pk=pk, is_active=True)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductPartialUpdateSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteAPIView(APIView):
    @staticmethod
    def delete(request, pk):
        try:
            product = Product.objects.get(pk=pk, is_active=True)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.is_active = False
        product.save()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)