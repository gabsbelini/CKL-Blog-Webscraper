from django.shortcuts import render
from django.core.files import File
from .models import Subject, Article, Author

from .serializers import ArticleSerializer, SubjectSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from bs4 import BeautifulSoup
import urllib
import json
import os
import re


class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all().order_by('created_date')
    serializer_class = ArticleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('subject', 'author')
    http_method_names = ['get']


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    http_method_names = ['get']


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


def index(request):
    def extract_data():
        for block in blocks:
            print(block.find('h2').text)
            # Checks if article has already been added
            if Article.objects.filter(title=block.find('h2').text).exists():
                continue
            article = Article()
            article.title = block.find('h2').text
            article.url = block.find('h2').a['href']
            article.slug = re.findall('/([^/]*)/$', block.find('h2').a['href'])[0]
            article.publish_date = block.find('time')['datetime']
            if block.find('p', attrs={'class': 'excerpt'}):
                article.text = block.find('p', attrs={'class': 'excerpt'}).text[:200]
            else:
                article.text = ''
            # Checks if author isn't in database yet and adds it
            if not Author.objects.filter(name=block.find('a', attrs={'rel': 'author'}).text).exists():
                author = Author(name=block.find('a', attrs={'rel': 'author'}).text)
                author.save()
                article.author = Author.objects.latest('id')
            else:
                article.author = Author.objects.get(name=block.find('a', attrs={'rel': 'author'}).text)
            # Checks if article has a subject
            if block.find('a', attrs={'class': 'tag'}):
                if not Subject.objects.filter(name=block.find('a', attrs={'class': 'tag'}).text).exists():
                    subject = Subject(name=block.find('a', attrs={'class': 'tag'}).text)
                    subject.save()
                    article.subject = Subject.objects.latest('id')
                else:
                    article.subject = Subject.objects.get(name=block.find('a', attrs={'class': 'tag'}).text)
            else:
                article.subject = Subject.objects.get(name='null')
            if block.find('img'):
                temp_image = urllib.request.urlretrieve(block.find('img')['data-src'])
                article.hero_image.save(os.path.basename(block.find('img')['data-src']), File(open(temp_image[0], 'rb')))
            article.save()
    for page_number in range(1,11):
        if page_number == 1:
            html = urllib.request.urlopen('https://techcrunch.com/')
        else:
            html = urllib.request.urlopen('https://techcrunch.com/page/'+ str(page_number))
        soup = BeautifulSoup(html, 'html.parser')
        blocks = [block for block in soup.find_all('li', attrs={'class': 'river-block'})]
        extract_data()
    return render(request, 'index.html')
