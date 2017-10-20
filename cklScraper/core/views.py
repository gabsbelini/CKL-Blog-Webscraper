from django.shortcuts import render
from django.core.files import File
from .models import Subject, Article, Author

from bs4 import BeautifulSoup
import urllib
import json
import os
import re


def index(request):
    html = urllib.request.urlopen('https://techcrunch.com/page/2')
    soup = BeautifulSoup(html, 'html.parser')
    blocks = [block for block in soup.find_all('li', attrs={'class': 'river-block'})]

    def extract_data():
        for block in blocks:
            # Checks if article has already been added
            if Article.objects.filter(title=block.find('h2').text).exists():
                continue
            article = Article()
            article.title = block.find('h2').text
            article.url = block['data-permalink']
            article.slug = re.findall('https://techcrunch.com/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.*)/', block['data-permalink'])[0]

            article.publish_date = block.find('time')['datetime']
            article.text = block.find('p', attrs={'class': 'excerpt'}).text[:200]
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

    extract_data()
    return render(request, 'index.html', {'data': data})
