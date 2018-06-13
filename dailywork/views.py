# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from work import *
from django.http import HttpResponse
from models import *
from django.views import generic
# 引入我们创建的表单类
from .forms import Form1, Jmeter_F, task_F


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


def task(request):
    if request.method == "GET":
        project_name = request.path.split('/')[-1]
        # project_name = request.GET.get('name')
        Task.objects.filter(project_name__contains=project_name).update(is_finish=1)
        # return render_to_response("home.html")


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
    return render(request, "perf.html", {"form": f})


def daily_task(request):
    tds_data = tds_req()
    if tds_data['message'] == 'error':
        raise Exception, 'tds return error'
    data = tds_data['data']
    if request.method == "GET":
        project_name = request.path.split('/')[-1]
        # project_name = request.GET.get('name')
        Task.objects.filter(project_name=project_name).update(is_finish=1)
    input_data = Task.objects.all().filter(is_finish=0)
    for each in input_data:
        project_name = each.project_name
        affect_app = each.affect_app
        branch = each.branch
        developer = each.developer
        submitdate = str(each.submitdate)
        releasedate = str(each.releasedate)
        is_finish = each.is_finish
        data[project_name] = {'type':'self','is_finish':is_finish,'affect_app':affect_app,
                              'affect_api': branch, 'submitter': developer, 'submitDate': submitdate,
                              'releaseETA': releasedate}
    if tds_data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('daily_work.html', {'text': 'wwooo!!! error'})
    if request.method == "POST":
        task = task_F(request.POST)
        if task.is_valid():
            task.save()
        else:
            print task.errors
            return render(request, "daily_work.html", {"error": task.errors, "form": task, "data": data})
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        task = task_F()
        return render(request, "daily_work.html", {"form": task, "data": data})
    return render(request, "daily_work.html", {"form": task, "data": data})
