from django.db import models
from member.models import Profile


# Create your models here.
class Page(models.Model):
    subject = models.CharField(max_length=50, blank=False, default='標題')
    author = models.ForeignKey(Profile)
    datetime = models.DateTimeField(blank=False)
    content = models.TextField()


class Article(models.Model):
    category = models.CharField(max_length=2, blank=False, default='一般')
    subject = models.CharField(max_length=50)
    author = models.ForeignKey(Profile)
    datetime = models.DateTimeField(blank=False)
    content = models.TextField()
