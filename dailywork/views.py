# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response,render
from work import *
from django.http import HttpResponse
from models import *
from django.views import generic
# 引入我们创建的表单类
from .forms import Form1,Jmeter_F,task_F
# Create your views here.


# @login_required()
def daily(request):
    data = tds_req()
    if data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('daily_work.html', {'text': 'wwooo!!! error'})
    else:
        return render_to_response('daily_work.html', {'text': 'wwooo!!!', 'data': data['data']})


class ServerListView(generic.ListView):
    model = CatServerInfo
    template_name = 'test_list.html'


class ServerDetailView(generic.DetailView):
    model = CatServerInfo
    template_name = 'test_detail.html'
    # pk_url_kwarg = 'id'


def perf(request):
    if request.method == "POST":
        f = Jmeter_F(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
        else:
            return render(request, "perf.html", {"error": f.errors, "form": f})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        f = Jmeter_F()
        return render(request, "perf.html", {"form": f})
    return render(request, "perf.html",{"form": f})


def daily_task(request):
    data = tds_req()
    if data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('daily_work.html', {'text': 'wwooo!!! error'})
    if request.method == "POST":
        task = task_F(request.POST)
        if task.is_valid():
            print(task.cleaned_data)
        else:
            return render(request, "daily_work.html", {"error": task.errors, "form": task})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        task = task_F()
        return render(request, "daily_work.html", {"form": task,"data":data['data']})
    return render(request, "daily_work.html",{"form": task,"data":data['data']})