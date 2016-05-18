"""ask_bulavintsev URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views as basic
from django.conf import settings

#only dev!!!!!!!!!!!!!

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    #url(r'^$', basic.wsgi, name='wsgi'),

    url(r'^hot/$', basic.hot, name='hot'),
    url(r'^question/(?P<id>[0-9]+)/$', basic.question_detail, name='question'),
    url(r'^tag/(?P<id>[0-9]+)/$', basic.tag, name='tag'),
    url(r'^login/$', basic.login, name='login'),
    url(r'^logout/$', basic.log_out, name='logout'),
    url(r'^register/$', basic.register, name='register'),
    url(r'^ask/$', basic.ask, name='ask'),
    url(r'^answer/$', basic.answer, name='answer'),
    url(r'^$', basic.index, name='index'),
]
#only dev!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()