#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http                    import Http404
from django.shortcuts               import render_to_response
from django.template                import TemplateDoesNotExist

def home(request):    
    # Render template without any argument
    return render_to_response('index.html')

def partial(request, partial_name=None):    
    template_name = 'partials/' + partial_name + '.html';
    try:
        return render_to_response(template_name)
    except TemplateDoesNotExist:
        raise Http404