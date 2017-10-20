from django.shortcuts import render
from django.core.files import File
from .models import Subject, Article, Author

from bs4 import BeautifulSoup
import urllib
import json
import os


def index(request):
    titles_list, authors_list, tags_list, dates_list, texts_list, imgs_list = [], [], [], [], [], []
    tags_list.append('LALALA')
    html = urllib.request.urlopen('https://techcrunch.com/')
    soup = BeautifulSoup(html, 'html.parser')

    for anchor in soup.find_all('h2', attrs={'class': 'post-title'}):
        titles_list.append(anchor.text)
    for name in soup.find_all('a', attrs={'rel': 'author'}):
        authors_list.append(name.text)
    for tag in soup.find_all('div', attrs={'class': 'tags'}):
        tags_list.append(tag.text.strip('\n'))
    for dates in soup.find_all('time', attrs={'class': 'timestamp'}):
        dates_list.append(dates['datetime'])
    for text_summary in soup.find_all('p', attrs={'class': 'excerpt'}):
        texts_list.append(text_summary.text[:200])
    for img in soup.find_all('img'):
        if 'data-src' in img.attrs:
            if img['data-src'].startswith('https://tctechcrunch20'):
                imgs_list.append(img['data-src'])
    print(tags_list)
    print(len(titles_list))
    print(len(authors_list))
    print(len(tags_list))
    print(len(dates_list))
    print(len(texts_list))
    print(len(imgs_list))

    for x in range(len(titles_list)):
        if not Article.objects.filter(title=titles_list[x]).exists():
            article = Article()
            article.title = titles_list[x]
            if not Subject.objects.filter(name=tags_list[x]).exists():
                subject = Subject()
                subject.name = tags_list[x]
                subject.save()
                article.subject = Subject.objects.latest('id')
            else:
                print(tags_list[x])
                article.subject = Subject.objects.get(name=tags_list[x])
            if not Author.objects.filter(name=authors_list[x]).exists():
                author = Author()
                author.name = authors_list[x]
                author.save()
                article.author = Author.objects.latest('id')
            else:
                article.author = Author.objects.get(name=authors_list[x])
            article.publish_date = dates_list[x]
            article.text = texts_list[x]
            temp_image = urllib.request.urlretrieve(imgs_list[x])
            article.hero_image.save(os.path.basename(imgs_list[x]), File(open(temp_image[0], 'rb')))
            article.save()

    return render(request, 'index.html')
