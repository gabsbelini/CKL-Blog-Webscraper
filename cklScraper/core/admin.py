from django.contrib import admin
from .models import Subject, Author, Article


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subject', 'publish_date', 'author']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Subject)
