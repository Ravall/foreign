# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from frontend.views import _get_tag_articles
from control import utils

def index(request):
    data = _get_tag_articles('words')
    data['category'] = 'training'
    return render_to_response(
        'frontend/training/words.html',
        data,
        context_instance=RequestContext(request)
    )

def word(request, word):
    data = _get_tag_articles('words')
    content = utils.api_request(
        'engdel/article/{0}.json'.format(word)
    )
    if not content:
        raise Http404
    content = json.loads(content)
    data['about_content'] = content
    data['category'] = 'training'
    return render_to_response(
        'frontend/training/word.html',
        data,
        context_instance=RequestContext(request)
    )