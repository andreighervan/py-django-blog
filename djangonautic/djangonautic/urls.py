from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from articles import views as article_views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^articles/', include('articles.urls')),
    url(r'^$', article_views.article_list, name='home')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
