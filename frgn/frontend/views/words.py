

def index(request, article_name):
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