from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article_list, name='list'),
    url(r'^create/$', views.article_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='detail'),
]

urlpatterns += staticfiles_urlpatterns()
