from django.contrib import admin
from .models import Page, Article


# Register your models here.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['subject', 'content']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['subject', 'content']
