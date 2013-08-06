# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from control import utils

def index(request):
    theoretics = utils.api_request(
        'engdel/article/tag/{0}.json'.format('theoretics')
    )

    return render_to_response(
        'frontend/index.html',
        {
            'theoretics':json.loads(theoretics)
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
        {'content':content},
        context_instance=RequestContext(request)
    )