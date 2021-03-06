from __future__ import unicode_literals
from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from frontend import views
from frontend.views import words,books,school,sitemap

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
        r'^school/$', school.school,
        {'article_name': 'o_nas_kursy_daisy'}, name='school'
    ),
    url(
        r'^school/vakansii_kursy_daisy$', school.school_job,
        {'article_name': 'vakansii_kursy_daisy'}, name='school_job'
    ),
    url(
        r'^school/study$', school.school_study, name='school_study'
    ),
    url(
        r'^school/(?P<article_name>[0-9a-z_]+)', school.school,
        name='school_article'
    ),
    url(
        r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': sitemap.sitemaps}
    ),
    url(
        r'^training/$', views.training, name='training'
    ),
    url(
        r'^words/$', words.index, name='training_words'
    ),
    url(
        r'^words/(?P<word>[0-9a-z_]+)/$', words.word, name='word_list'
    ),
    url(
        r'^books/$', books.index, name='training_books'
    ),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
