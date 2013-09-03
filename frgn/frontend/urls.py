from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from frontend import views

# pylint: disable=C0103
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(
        r'^theoretics/',
        views.theoretics,
        name='theoretics'
    ),
    url(
        r'^practice/',
        views.practice,
        name='practice'
    ),
    url(
        r'^linguistics/',
        views.linguistics,
        name='linguistics'
    ),
    url(
        r'^methods/',
        views.methods,
        name='methods'
    ),
    url(
        r'^psi/',
        views.psi,
        name='psi'
    ),
    url(
        r'^article/(?P<article_name>[0-9a-z_]+)$',
        views.article,
        name='article'
    ),
    url(
        r'^page/about$',
        views.page,
        name='page'
    ),
    url(r'^school/$', views.school, {'article_name': 'o_nas_kursy_daisy'}, name='school'),
    url(r'^school/(?P<article_name>[0-9a-z_]+)', views.school, name='school_article'),



)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
