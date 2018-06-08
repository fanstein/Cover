# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from work import *
from models import *
from django.views import generic
# Create your views here.


# @login_required()
def index(request):
    data = tds_req()
    if data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('index.html', {'text': 'wwooo!!! error'})
    else:
        return render_to_response('index.html', {'text': 'wwooo!!!', 'data': data['data']})


class ServerListView(generic.ListView):
    model = CatServerInfo
    template_name = 'test_list.html'


class ServerDetailView(generic.DetailView):
    model = CatServerInfo
    template_name = 'test_detail.html'
    # pk_url_kwarg = 'id'
