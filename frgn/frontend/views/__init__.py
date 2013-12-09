# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.cache import cache_page
from control import utils
from django.conf import settings
from frontend.models import ContactForm
from django.contrib import messages
from django.shortcuts import redirect

def _get_tag_articles(tag):
    tag_articles = utils.api_request(
        'engdel/article/tag/{0}.json'.format(tag)
    )
    tag_articles = json.loads(tag_articles)
    return {
        'category': tag,
        tag: tag_articles
    }


def theoretics(request):
    theoretics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('theoretics')
    )
    theoretics = json.loads(theoretics)
    return render_to_response(
        'frontend/theoretics.html',
        {
            'category': 'theoretics',
            'theoretics': theoretics
        },
        context_instance=RequestContext(request)
    )


def practice(request):
    practice = utils.api_request(
        'engdel/article/tag/{0}.json'.format('practice')
    )
    practice = json.loads(practice)
    return render_to_response(
        'frontend/practice.html',
        {
            'category': 'practice',
            'practice': practice
        },
        context_instance=RequestContext(request)
    )

def linguistics(request):
    linguistics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('linguistics')
    )
    linguistics = json.loads(linguistics)
    return render_to_response(
        'frontend/linguistics.html',
        {
            'category': 'linguistics',
            'linguistics': linguistics
        },
        context_instance=RequestContext(request)
    )

def methods(request):
    return render_to_response(
        'frontend/methods.html',
        _get_tag_articles('methods'),
        context_instance=RequestContext(request)
    )

def psi(request):
    return render_to_response(
        'frontend/psi.html',
        _get_tag_articles('psi'),
        context_instance=RequestContext(request)
    )



def index(request):
    # теоретические материалы
    theoretics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('theoretics')
    )
    theoretics = json.loads(theoretics)
    # практические материалы
    practice = utils.api_request(
        'engdel/article/tag/{0}.json'.format('practice')
    )
    practice = json.loads(practice)
    # языкознание
    linguistics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('linguistics')
    )
    linguistics = json.loads(linguistics)
    # методолгоия
    methods = _get_tag_articles('methods')
    #психология
    psi = _get_tag_articles('psi')
    return render_to_response(
        'frontend/index.html',
        {
            'theoretics': theoretics[0:settings.FRON_MAX_COUNT_ARTICLES],
            'practice': practice[0:settings.FRON_MAX_COUNT_ARTICLES],
            'linguistics': linguistics[0:settings.FRON_MAX_COUNT_ARTICLES],
            'methods': methods['methods'][0:settings.FRON_MAX_COUNT_ARTICLES],
            'psi': psi['psi'][0:settings.FRON_MAX_COUNT_ARTICLES],
        },
        context_instance=RequestContext(request)
    )



def article(request, article_name):
    def get_main_tag(tags):
        for tag in settings.MAIN_CATEGORY:
            if tag in tags:
                return tag
        return ''

    content = utils.api_request(
        'engdel/article/{0}.json'.format(article_name)
    )
    if not content:
        raise Http404
    content = json.loads(content)
    if not get_main_tag(content['tags']):
        raise Http404
    return render_to_response(
        'frontend/article.html',
        {
            'content': content,
            'category': get_main_tag(content['tags']),
        },
        context_instance=RequestContext(request)
    )

def training(request):
    return render_to_response(
        'frontend/training/index.html',
        {'category':'training'},
        context_instance=RequestContext(request)
    )
