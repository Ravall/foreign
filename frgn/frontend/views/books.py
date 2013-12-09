# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from frontend.views import _get_tag_articles
from control import utils

def index(request):
    data = {'category':'training'}
    return render_to_response(
        'frontend/training/books.html',
        data,
        context_instance=RequestContext(request)
    )