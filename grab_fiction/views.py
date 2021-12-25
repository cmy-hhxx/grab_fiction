from django.shortcuts import render
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .models import Novel

def grab_novel(request):
    base_url = 'http://www.qu-la.com'
    target_final = "http://www.qu-la.com/booktxt/69650309116/"
    target = 'http://www.qu-la.com/booktxt/69650309116/23992348116.html'
    target2 = 'http://www.qu-la.com/booktxt/69650309116/23992349116.html'
    result = requests.get(url=target_final)
    html = result.text

    brief = BeautifulSoup(html)
    texts = brief.find_all('div', class_ ='txt')
    links = brief.find_all('ul', class_ ='cf')

    a_brief = BeautifulSoup(str(links[1]))


    a = a_brief.find_all('a')

    for each in a:
        novel = Novel()
        novel.title = each.string
        novel.url = base_url + each.get('href')
        res = requests.get(url=novel.url)
        html = res.text
        novel.content = BeautifulSoup(html).find_all('div', class_ ='txt')
        novel.save()

    #url_final = base_url + a[0].get('href')
    #title = a[0].string
    return HttpResponse(title)

def novel_show(request):
    fictions = Novel.objects.all()
    return HttpResponse(fictions)


