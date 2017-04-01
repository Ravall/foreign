# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    data = {'category':'training'}
    return render_to_response(
        'frontend/training/books.html',
        data,
        context_instance=RequestContext(request)
    )