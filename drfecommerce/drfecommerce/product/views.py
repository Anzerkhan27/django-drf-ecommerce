from django.shortcuts import get_object_or_404, render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many = True)
        return Response(serializer.data)



class BrandViewSet(viewsets.ViewSet):
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many = True)
        return Response(serializer.data)
    

class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    lookup_field = "slug"

    def list(self, request):
        serializer = ProductSerializer(self.queryset.filter(is_active = True), many = True)
        return Response(serializer.data)    
    
    
    def retrieve(self, request, slug=None):
        product = get_object_or_404(self.queryset, slug=slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    @action(methods=["get"], detail=False, url_path=r"category/(?P<category>\w+)/all", url_name="all",)
    def list_product_by_category(self, request, category=None):
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)

