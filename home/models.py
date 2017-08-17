from django.db import models
from django.contrib.auth.models import User


class Page(models.Model):
    title = models.CharField(max_length=50, default='標題')
    author = models.ForeignKey(User)
    datetime = models.DateTimeField()
    content = models.TextField()


class Article(models.Model):
    category = models.CharField(max_length=2, default='一般')
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User)
    datetime = models.DateTimeField(blank=False)
    content = models.TextField()
