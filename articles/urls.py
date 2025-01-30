from django.urls import path
from . import views

app_name = "articles"
urlpatterns = [
    path("", views.ArticleListAPIView.as_view()),
    path("<int:pk>/", views.article_detail),
]
