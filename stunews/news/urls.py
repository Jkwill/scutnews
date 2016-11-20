from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.newslists, name='homepage'),
    url(r'^(?P<news_id>\d+)$', views.news, name='news'),
    # url(r'^login/$', auth_views.login, {'template_name': 'edit/login.html', 'redirect_field_name': r'/scutnews/edit/'},
    #     name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'edit/login.html'},
        name='login'),
    url(r'^edit/$', views.editnews, name='edit')
]
