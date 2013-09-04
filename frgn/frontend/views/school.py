# -*- coding: utf-8 -*-
import json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from control import utils
from frontend.models import ContactForm, StudentForm
from django.contrib import messages
from django.shortcuts import redirect
from frontend.views import _get_tag_articles

def school(request, article_name):
    data = _get_tag_articles('school')
    content = utils.api_request(
        'engdel/article/{0}.json'.format(article_name)
    )
    if not content:
        raise Http404
    content = json.loads(content)
    data['about_content'] = content
    return render_to_response(
        'frontend/school/school.html',
        data,
        context_instance=RequestContext(request)
    )

def school_job(request, article_name):
    data = _get_tag_articles('school')
    content = utils.api_request(
        'engdel/article/{0}.json'.format(article_name)
    )
    if not content:
        raise Http404
    content = json.loads(content)
    data['about_content'] = content

    if request.method == 'POST': # пару проверок формы
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(
                request, messages.INFO,
                'Ваши данные сохранены. Мы обязательно с вами свяжемся.'
            )
            form.save() # сохраняем нашу форму в базу
            return redirect('school_job')
    else:
        form = ContactForm()
    data['form'] = form
    return render_to_response(
        'frontend/school/school_job.html',
        data,
        context_instance=RequestContext(request)
    )

def school_study(request):
    data = _get_tag_articles('school')
    data['page'] = 'study'
    if request.method == 'POST': # пару проверок формы
        form = StudentForm(request.POST)
        if form.is_valid():
            messages.add_message(
                request, messages.INFO,
                'Ваши данные сохранены. Мы обязательно с вами свяжемся.'
            )
            form.save() # сохраняем нашу форму в базу
            return redirect('school_study')
    else:
        form = StudentForm()
    data['form'] = form
    return render_to_response(
        'frontend/school/school_study.html',
        data,
        context_instance=RequestContext(request)
    )
