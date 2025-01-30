from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# 게시글 리스트 보기 및 글 생성하기
# 함수형일 때는 @api_view를 꼭 적어줘야 함
@api_view(["GET", "POST"])
def article_list(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data) # data에 POST 데이터를 넣어줘요
        if serializer.is_valid(): # 만약 serializer 값이 유효하다면,
            serializer.save() # article 생성
            return Response(serializer.data, status=201) # api 201(created)를 반환
        return Response(serializer.errors, status=400) # 만약 제목을 빼먹었거나 하면 error 반환


# 게시글 상세 목록
@api_view(["GET"])
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk) # 없는 pk 값을 불렀을 때, 404 화면이 뜨도록
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
