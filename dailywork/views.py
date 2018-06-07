# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from work import *
# Create your views here.


@login_required()
def index(request):
    data = tds_req()
    if data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('index/index.html', {'text': 'wwooo!!! error'})
    else:
        return render_to_response('index/index.html', {'text': 'wwooo!!!', 'data': data['data']})
