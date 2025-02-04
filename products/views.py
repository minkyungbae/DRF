from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.cache import cache

from .models import Product
from .serializers import ProductSerializer

@api_view(["GET"])
def product_list(request):
    cache_key = "product_list" # cache_key 만들기
    cache.get(cache_key) # cache_key 가져오기
    
    if not cache.get(cache_key): # cache에서 get 했는데, 없다면
        print("cache miss")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_reponse = serializer.data
        cache.set("product_list", json_reponse, 20) # key와 value를 만들기, 20초 후에 캐싱 없애기
        
    response_data = cache.get(cache_key) # cache에서 get 했는데, 있다면
    return Response(response_data)
