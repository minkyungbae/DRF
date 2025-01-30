from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView


# 게시글 상세 목록
@api_view(["GET","PUT", "DELETE"])
def article_detail(request, pk):
    if request.method == "GET":
        article = get_object_or_404(Article, pk=pk) # 없는 pk 값을 불렀을 때, 404 화면이 뜨도록
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 게시글 수정하기
    elif request.method == "PUT":
        article = get_object_or_404(Article, pk=pk) # 조회한 article
        serializer = ArticleSerializer(article, data=request.data, partial=True) # article에 입력한 data를 넣고, 개별 변경 가능
        if serializer.is_valid(raise_exception=True): # 만약 serializer 값이 유효하다면, 예외 발생 True
            serializer.save() # 저장하고 수정.
            return Response(serializer.data) # 그 수정된 값을 반환
    
    # 게시글 삭제하기
    elif request.method == "DELETE":
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleListAPIView(APIView):  # GET, POST만 정의돼 있어서 그 외의 method엔 작동 X
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ArticleSerializer(data=request.data) # data에 POST 데이터를 넣어줘요
        if serializer.is_valid(raise_exception=True): # 만약 serializer 값이 유효하고, 예외 발생 True
            serializer.save() # article 생성
            return Response(serializer.data, status=201) # api 201(created)를 반환