from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("article",)
        
    # 댓글 목록에서 article 없애기
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("article")
        return ret

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        

class ArticleDetailSerializer(ArticleSerializer):
    # 모든 comments들을 CommentSerializer에 넘겨서 직렬화한 후, fields 추가해 줘!
    comments = CommentSerializer(many=True, read_only=True) # 오버라이딩
    # 댓글 갯수
    comments_count = serializers.IntegerField(source="comments.count", read_only=True) #.count가 ORM 함수    
        