from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView

class ArticleListAPIView(APIView):  # GET, POST만 정의돼 있어서 그 외의 method엔 작동 X
    # 글 목록 보기
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    # 글 작성하기
    def post(self, request):
        serializer = ArticleSerializer(data=request.data) # data에 POST 데이터를 넣어줘요
        if serializer.is_valid(raise_exception=True): # 만약 serializer 값이 유효하고, 예외 발생 True
            serializer.save() # article 생성
            return Response(serializer.data, status=201) # api 201(created)를 반환
        
        
class ArticleDetailAPIView(APIView):
    # 상세 목록 보기
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk) # 없는 pk 값을 불렀을 때, 404 화면이 뜨도록
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 글 수정하기
    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk) # 조회한 article
        serializer = ArticleSerializer(article, data=request.data, partial=True) # article에 입력한 data를 넣고, 개별 변경 가능
        if serializer.is_valid(raise_exception=True): # 만약 serializer 값이 유효하다면, 예외 발생 True
            serializer.save() # 저장하고 수정.
            return Response(serializer.data) # 그 수정된 값을 반환
    
    # 글 삭제하기
    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class CommentListAPIView(APIView):
    # 특정 article에 있는 댓글 조회하기
    def get(self, request, article_pk):
        # Article 모델에서 찾아와요. 근데 Article 모델에는 comment가 없잖아요?(역참조) ⬇️
        article = get_object_or_404(Article, pk=article_pk)
        # 그래서 Comment 모델의 매니저인 "comments"를 데리고 와서, 해당 글에 있는 comments들을 데려와요 ⬇️
        comments = article.comments.all() # 조회된 comments들을
        serializer = CommentSerializer(comments, many=True) # serializer에 넣어줬어요. 많으니까 many=True
        return Response(serializer.data)
    
    # 댓글 생성하기
    def post(self, request, article_pk):
        article = get_object_or_404(Article, pk=article_pk) # 역참조
        serializer = CommentSerializer(data=request.data) # data에 POST 받은 값을 넣어줘요, 여기엔 content 값만 있어요
        if serializer.is_valid(raise_exception=True): # 값이 유효하다면, 예외 발생 True
            serializer.save(article=article) # 저장할 때, 필요한 나머지 데이터를 article로 채워줌
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        