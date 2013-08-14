# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.cache import cache_page
from control import utils
from django.conf import settings


def theoretics(request):
    theoretics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('theoretics')
    )
    theoretics = json.loads(theoretics)
    return render_to_response(
        'frontend/theoretics.html',
        {
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
            'practice': practice
        },
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
    return render_to_response(
        'frontend/index.html',
        {
            'theoretics': theoretics[0:settings.FRON_MAX_COUNT_ARTICLES],
            'practice': practice[0:settings.FRON_MAX_COUNT_ARTICLES],
        },
        context_instance=RequestContext(request)
    )


def article(request, article_name):
    content = utils.api_request(

        'engdel/article/{0}.json'.format(article_name)
    )
    if not content:
        raise Http404
    content = json.loads(content)
    return render_to_response(
        'frontend/article.html',
        {
            'content': content
        },
        context_instance=RequestContext(request)
    )