from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^', include('frontend.relink_urls')),
    url(r'^', include('frontend.urls')),
    url(r'', include('robots_txt.urls')),
    url(r'^', include('favicon.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
