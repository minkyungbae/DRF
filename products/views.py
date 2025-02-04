from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

@api_view(["GET"])
def product_list(request):
    products = Product.pbjects.all()
    serializer = ProductSerializer(products, many=True)
    json_reponse = serializer.data
    return Response(json_reponse)
