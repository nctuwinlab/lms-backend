from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/(?P<page>[0-9]*)/?$',
        views.ArticleList.as_view(), name='articles'),
]
