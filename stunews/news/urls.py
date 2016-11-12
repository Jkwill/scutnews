from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.newslists, name='homepage'),
    url(r'^(?P<news_id>\d+)$', views.news, name='news')
]
