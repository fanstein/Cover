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
    template_name = 'learn/test_list.html'


class ServerDetailView(generic.DetailView):
    model = CatServerInfo
    template_name = 'learn/test_detail.html'
    # pk_url_kwarg = 'id'


def get_task(data):
    """
    数据库获取手动输入任务
    :param data:
    :return:
    """
    input_data = Task.objects.all().filter(is_finish=0)
    for each in input_data:
        project_name = each.project_name
        cp4 = each.cp4
        affect_app = each.affect_app
        branch = each.branch
        developer = each.developer
        submitdate = str(each.submitdate)
        releasedate = str(each.releasedate)
        is_finish = each.is_finish
        data[project_name] = {'type': 'self', 'cp4': cp4, 'is_finish': is_finish, 'affect_app': affect_app,
                              'affect_api': branch, 'submitter': developer, 'submitDate': submitdate,
                              'releaseETA': releasedate}
    return data


def get_perf_result(request):
    """
    获取测试结果
    :param request:
    :return:
    """
    data = []
    if request.method == 'GET' or request.method == 'POST':
        result = PerfResult.objects.all()
        total = result.count()
        for each in result:
            id = each.id
            response = each.response
            tps = each.tps
            success = each.success_percent
            exec_time = each.exec_time
            appid = each.appid
            name = each.name
            path =each.path
            attribute = each.attribute
            data.append({'id':id, 'name':appid+':'+name, 'success':success, 'TPS':tps, 'time':response,'create_time':str(exec_time),'attribute':attribute})
        res = {'total':total,'rows':data}
        return HttpResponse(json.dumps(res, ensure_ascii=False), content_type='application/json; charset=utf-8')


def perf(request):
    """
    性能表单
    :param request:
    :return:
    """
    # result = PerfResult.objects.all()
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


def deploy(request):
    """
    发布通知
    :param request:
    :return: work.development()
    """
    try:
        appid = request.GET.get('appid')
        env = request.GET.get('env')
    except Exception as e:
        raise e,'request get attribute error'
    data = development(appid=appid, env=env)
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type='application/json; charset=utf-8')


# show create table tester.task;
def daily_task(request):
    """
    dail.html对应的后台应用
    :param request:
    :return:
    """
    tds_data = tds_req()
    data = tds_data['data']
    # data = {}
    if tds_data['message'] == 'error':
        print 'response error!!!'
        return render_to_response('daily_work.html', {'text': 'wwooo!!! error'})
    # 通过form save保存数据到数据库
    if request.method == "POST":
        task = task_F(request.POST)
        if task.is_valid():
            task.save()
        else:
            print task.errors
            return render(request, "daily_work.html", {"error": task.errors, "form": task, "data": data})
    # 修改本地任务是否完成
    elif request.method == "GET":
        task = task_F()
        project_name = request.path.split('/')[-1]
        Task.objects.filter(project_name=project_name).update(is_finish=1)
    # 加载时，form为空
    else:
        # 如果不是post提交数据，就不传参数创建对象，并将对象返回给前台，直接生成input标签，内容为空
        task = task_F()
        return render(request, "daily_work.html", {"form": task, "data": data})
    data = get_task(data)
    return render(request, "daily_work.html", {"form": task, "data": data})
