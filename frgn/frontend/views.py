# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.cache import cache_page
from control import utils


def index(request):
    theoretics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('theoretics')
    )
    theoretics = json.loads(theoretics)
    return render_to_response(
        'frontend/index.html',
        {
            'theoretics': theoretics[0:10],
            'theoretics_len': len(theoretics)
        },
        context_instance=RequestContext(request)
    )

@cache_page(60 * 5)
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