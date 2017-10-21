from rest_framework import serializers

from .models import Article, Subject


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ('id', 'title', 'url', 'slug', 'author', 'subject', 'publish_date', 'hero_image', 'text')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('name', 'color')
