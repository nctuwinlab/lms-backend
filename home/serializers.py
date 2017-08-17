from rest_framework import serializers

from member.serializers import UserSerializer
from .models import Page, Article


class PageSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=50, default='標題')
    author = UserSerializer()
    datetime = serializers.DateTimeField()
    content = serializers.CharField()

    class Meta:
        model = Page
        field = ['title', 'author', 'datetime', 'content']


class ArticleSerializer(serializers.ModelSerializer):

    category = serializers.CharField(max_length=2, default='一般')
    title = serializers.CharField(max_length=50)
    author = UserSerializer()
    datetime = serializers.DateTimeField()
    content = serializers.CharField()

    class Meta:
        model = Article
        field = ['category', 'title', 'author', 'datetime', 'content']

    