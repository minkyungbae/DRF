from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# 게시글 리스트 보기
# 함수형일 때는 @api_view를 꼭 적어줘야 함
@api_view(["GET"])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


# 게시글 상세 목록
@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk) # 없는 pk 값을 불렀을 때, 404 화면이 뜨도록
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
