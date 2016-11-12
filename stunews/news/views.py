# coding: utf-8
from django.shortcuts import render


def newslists(request):
    return render(request, 'newslists.html')


def news(request, news_id):
    return render(request, 'news.html', {'news_id': news_id})
