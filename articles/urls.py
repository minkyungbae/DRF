from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view()),
    path("<int:pk>/", views.ArticleDetailAPIView.as_view()),
    
    # 특정 Article의 댓글 조회
    path("<int:article_pk>/comments/",
         views.CommentListAPIView.as_view(),
         name="comment_list"),
    
    # comment 삭제하기
    path("comments/<int:comment_pk>/",
         views.CommentDetailAPIView.as_view(),
         name="comment_detail"),
]
