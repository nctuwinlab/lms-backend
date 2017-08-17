from collections import OrderedDict

from django.contrib.auth.models import User

from rest_framework import serializers

from member.serializers import UserSerializer
from .models import Page, Article


class ContentSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):

        ret = OrderedDict()
        
        for field in self._readable_fields:

            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            if field.field_name == 'author':
                user = field.to_representation(attribute)
                ret[field.field_name] = user['username']
            else:
                ret[field.field_name] = field.to_representation(attribute)

        return ret


class PageSerializer(ContentSerializer):

    title = serializers.CharField(max_length=50, default='標題')
    author = UserSerializer()
    datetime = serializers.DateTimeField()
    content = serializers.CharField()

    class Meta:
        model = Page
        fields = ['title', 'author', 'datetime', 'content']


class ArticleSerializer(ContentSerializer):

    category = serializers.CharField(max_length=2, default='一般')
    title = serializers.CharField(max_length=50)
    author = UserSerializer()
    datetime = serializers.DateTimeField()
    content = serializers.CharField()

    class Meta:
        model = Article
        fields = ['category', 'title', 'author', 'datetime', 'content']
