# -*- coding: utf-8 -*-
import json
from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse
from django.conf import settings
from control import utils

class ReversItem(object):
    def __init__(self, route_name, args=[]):
        self.route_name = route_name
        self.args = args

    def get_absolute_url(self):
        return reverse(self.route_name, args=self.args)

class CategorySitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return [
            ReversItem(category)
            for category in (settings.MAIN_CATEGORY+['school'])
        ]


class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def get_articles_url(self, category):
        tag_articles = utils.api_request(
            'engdel/article/tag/{0}.json'.format(category)
        )
        tag_articles = json.loads(tag_articles)
        return [art['name'] for art in tag_articles]

    def items(self):
        links = []
        for category in settings.MAIN_CATEGORY:
            links+=self.get_articles_url(category)
        sitemap_links = [
            ReversItem('article', [art_name])
             for art_name in links
        ]
        sitemap_links += [
            ReversItem('school_article', [art_name])
            for art_name in self.get_articles_url('school')
        ]
        sitemap_links += [ ReversItem('school_study') ]
        return sitemap_links


class SimplePage(Sitemap):
    changefreq = "daily"
    priority = 1

    def items(self):
        return [
            ReversItem(route_name) for route_name in ['index']
        ]


sitemaps = {
    'category': CategorySitemap,
    'articles': ArticleSitemap,
    'pages': SimplePage
}
