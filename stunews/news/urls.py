from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views
from .views import getNews


urlpatterns = [
    url(r'^$', views.newslists, name='homepage'),
    url(r'^(?P<news_id>\d+)$', views.news, name='news'),
    url(r'^login/$', auth_views.login, {'template_name': 'edit/login.html'},
        name='login'),
    url(r'^changepsd/$',auth_views.password_change,{'template_name': 'edit/psdchange.html',
                                                    'post_change_redirect': r'/scutnews/edit'
        }, name='psdchange'),
    url(r'^exit/$',auth_views.logout, {'template_name': 'edit/login.html'}, name='logout'),
    url(r'^edit/$', views.editnews, name='edit'),
    url(r'^getnews/$', views.getNews),

]
