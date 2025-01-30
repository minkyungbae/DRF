from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    # 1. 외래 키로, 댓글이 어느 글(Article)에 속하는지 알려줌
    # 2. Article 모델과 Comment 모델이 1:N의 관계를 가짐
    # 3. on_delete=models.CASCADE -> Article이 삭제되면, 댓글도 함께 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 댓글이 처음 생성됐을 때의 시간 기록
    updated_at = models.DateTimeField(auto_now=True) # 댓글이 수정될 때마다 시간 기록