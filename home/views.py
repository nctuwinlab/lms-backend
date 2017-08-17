from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from home.models import Page, Article
from home.serializers import PageSerializer, ArticleSerializer


class ArticleList(APIView):

    queryset = Article.objects.all()

    def get(self, request, page=None, format='None'):

        # If page is not assigned, we load article from 0 ~ 10
        page = 0 if not page else int(page)

        # 10 articles as a page, calculate limit range
        limit = [page * 10 + 1, (page + 1) * 10]

        articles = Article.objects.filter(
            pk__gte=limit[0], pk__lt=limit[1]
        )

        if not articles:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ArticleSerializer(articles, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
