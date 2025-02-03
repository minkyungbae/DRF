from django.shortcuts import render
from .models import Article, Comment
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, ArticleDetailSerializer, CommentSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# 글 목록 보기, 글 작성하기
class ArticleListAPIView(APIView):  # GET, POST만 정의돼 있어서 그 외의 method엔 작동 X
    
    # APIView에 있는 permission_classes를 활용해서 접근 제한하기
    permission_classes = [IsAuthenticated]
    
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
        

# 글 상세 목록 보기, 글 수정하기, 글 삭제하기      
class ArticleDetailAPIView(APIView):
    
    # APIView에 있는 permission_classes를 활용해서 접근 제한하기
    permission_classes = [IsAuthenticated]
    
    # 상세 목록 보기
    def get(self, request, pk):
        article = get_object_or_404(Article, pk=pk) # 없는 pk 값을 불렀을 때, 404 화면이 뜨도록
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    
    # 글 수정하기
    def put(self, request, pk):
        article = get_object_or_404(Article, pk=pk) # 조회한 article
        serializer = ArticleDetailSerializer(article, data=request.data, partial=True) # article에 입력한 data를 넣고, 개별 변경 가능
        if serializer.is_valid(raise_exception=True): # 만약 serializer 값이 유효하다면, 예외 발생 True
            serializer.save() # 저장하고 수정.
            return Response(serializer.data) # 그 수정된 값을 반환
    
    # 글 삭제하기
    def delete(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# 댓글 조회하기, 댓글 생성하기  
class CommentListAPIView(APIView):
    
    # APIView에 있는 permission_classes를 활용해서 접근 제한하기
    permission_classes = [IsAuthenticated]
    
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
        

# 댓글 삭제하기, 댓글 수정하기     
class CommentDetailAPIView(APIView):
    
    # APIView에 있는 permission_classes를 활용해서 접근 제한하기
    permission_classes = [IsAuthenticated]
    
    # 공통된 get_object를 수정하기 편하게끔 함수 만들어주기
    def get_object(self, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk)
    
    # 댓글 삭제하기
    def delete(self, request, comment_pk):
        comment = self.get_object(comment_pk) # Comment 모델을 통해서 comment 들고 와요
        comment.delete() # 가져온 comment를 삭제해주고,
        return Response(status=status.HTTP_204_NO_CONTENT) # 204를 보여주면 삭제 끝
    
    # 댓글 수정하기
    def put(self, request, comment_pk):
        comment = self.get_object(comment_pk)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# # 정참조 조회하기
# @api_view(["GET"])
# def check_sql(request):
#     from django.db import connection

#     comments = Comment.objects.all().select_related("article")
#     for comment in comments:
#         print(comment.article.title)

#     print("-" * 30)
#     print(connection.queries)

#     return Response()


# 역참조 조회하기
@api_view(["GET"])
def check_sql(request):
    from django.db import connection

    articles = Article.objects.all().prefetch_related("comments")
    for article in articles:
        comments = article.comments.all()
    for comment in comments:
        print(comment.id)

    print("-" * 30)
    print(connection.queries)

    return Response()