from django.shortcuts import render
from .models import Article
from django.http import JsonResponse, HttpResponse
from django.core import serializers

def article_list_html(request):
    articles = Article.objects.all()
    context = {"articles":articles}
    return render(request, "articles/article_list.html", context)

def json_01(request):
    articles = Article.objects.all()
    json_articles = []
    
    # Json 형식으로 만들어줌
    for article in articles:
        json_articles.append(
            {
                "title": article.title,
                "content": article.content,
                "created_at": article.created_at,
                "updated_at": article.updated_at,
            }
        )
    
    return JsonResponse(json_articles, safe=False)  # dict일 때는 safe를 안 적어도 되지만, 리스트여서 적어줌


def json_02(request):
    articles = Article.objects.all()
    res_data = serializers.serialize("json", articles)  # res = response
    return HttpResponse(res_data, content_type="application/json")