from django.shortcuts import render

from bs4 import BeautifulSoup
import urllib

def index(request):
    print('----------------TITLES-------------')
    html = urllib.request.urlopen('https://techcrunch.com/')
    soup = BeautifulSoup(html, 'html.parser')
    for anchor in soup.find_all('h2', attrs={'class': 'post-title'}):
        print(anchor.text)
    print('----------------NAMES-------------')
    for name in soup.find_all('a', attrs={'rel': 'author'}):
        print(name.text)
    print('----------------TAGS-------------')
    for tag in soup.find_all('a', attrs={'class': 'tag'}):
        print(tag.text)
    print('----------------TIMES-------------')
    for time in soup.find_all('time'):
        print(time['datetime'])
    for text in soup.find_all('p', attrs={'class': 'excerpt'}):
        print(text.text[:200])
        print()
    return render(request, 'index.html')
