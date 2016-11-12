# coding: utf-8
from django.shortcuts import render

from news.models import News


def newslists(request):
    news_list = News.objects.all()
    return render(request, 'newslists.html', {'news_lists': news_list})


def news(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news.html', {'news': news})


