# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import News
import json
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class Base(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Base, self).dispatch(request, *args, **kwargs)

def newslists(request):

    all_news = News.objects.all()
    news_list=[]
    for i in all_news[::-1]:
        news_list.append(i)
    if len(all_news) > 5:
        for i in all_news[::-1]:
            if len(news_list) <= 5:
                news_list.append(i)

    else:
        for i in all_news[::-1]:
            news_list = News.objects.all()

    return render(request, 'newslists.html', {'news_lists': news_list})

class Result(dict):
    """
    {
        key1 : value1,
        key2 : value2,
        statuscode : 1,
    }
    """

    def __init__(self):
        super(Result, self).__init__()
        self["statuscode"] = -1

    def setOK(self):
        self["statuscode"] = 0

    def setStatuscode(self, status):
        self["statuscode"] = status

    def setData(self, key, value):
        self[key] = value

    def setStatusCode(self, status_code):
        self["statuscode"] = status_code


def news(request, news_id):
    news = News.objects.get(id=news_id)
    return render(request, 'news.html', {'news': news})


def editnews(request):
    return render(request, 'edit/edit.html')

@csrf_exempt
def getNews(request):
    result = Result()
    page = json.loads(request.body.decode()).get('page')
    print(page)

    all_news = News.objects.all()
    temp=[]

    if len(all_news):
        result.setData("news", [])

        for newsList in all_news[::-1]:
            # temp.append({'id':newsList.id,'title':newsList.title,'tag':newsList.tag,'date':newsList.subdate,'readnum':newsList.readnum})
            temp.append({'id': newsList.id, 'title': newsList.title ,'date':str(newsList.subdate).split('+')[0]})
        endNum=page*10

        if len(all_news)<page*10:
            endNum=len(all_news)

        for i in range((page-1)*10,endNum):
            # result['news'].append({'id':temp[i]['id'],'title':temp[i]['title'],'tag':temp[i]['tag'],'date':temp[i]['date'],'readnum':temp[i]['readnum']})
            result['news'].append({'id': temp[i]['id'], 'title': temp[i]['title'],'date':temp[i]['date']})

    result.setOK()
    return HttpResponse(json.dumps(result))

