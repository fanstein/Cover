# coding=utf8
from django import forms
# from django.forms import ModelForm
from models import *

Method_Choice = (
    ('1', 'GET'),
    ('2', 'POST'),
    ('3', 'PUT'),
)


class Form1(forms.ModelForm):
    user = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    pwd = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'password'}))


class Jmeter_F(forms.ModelForm):
    api_name = forms.CharField(label='接口名', widget=forms.TextInput(attrs={'class': 'form-control'}))
    threads = forms.CharField(initial=10, label='线程数', widget=forms.TextInput(attrs={'class': 'form-control'}))
    duration = forms.IntegerField(initial=600, label='执行时长', widget=forms.TextInput(attrs={'class': 'form-control'}))
    host = forms.CharField(label='服务器地址', widget=forms.TextInput(attrs={'class': 'form-control'}))
    port = forms.IntegerField(initial=80, label='端口', widget=forms.TextInput(attrs={'class': 'form-control'}))
    method = forms.ChoiceField(choices=Method_Choice, label='方法', widget=forms.Select(attrs={'class': 'form-control'}))
    path = forms.CharField(label='路径', widget=forms.TextInput(attrs={'class': 'form-control'}))
    body_data = forms.CharField(label='报文', widget=forms.Textarea(attrs={'class': 'form-control', 'onchange': 'json_view()', 'id': 'json'}))

    class Meta:
        model = JmeterRuntime
        fields = ('api_name', 'threads', 'duration', 'host', 'port', 'method', 'path', 'body_data')


class task_F(forms.ModelForm):
    project_name = forms.CharField(label='项目名',widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    cp4 = forms.CharField(label='cp4', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    affect_app = forms.CharField(label='影响app', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    branch = forms.CharField(required=False, label='分支', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    developer = forms.CharField(required=False, label='开发', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}))
    submitdate = forms.DateField(label='提测日期', widget=forms.DateInput(attrs={'class': 'form-control form_date', 'autocomplete': 'off', 'data-date-format': 'yyyy-mm-dd',
               'data-link-format': 'yyyy-mm-dd'}))
    releasedate = forms.DateField(label='发布日期', widget=forms.DateInput(attrs={'class': 'form-control form_date', 'autocomplete': 'off', 'data-date-format': 'yyyy-mm-dd',
               'data-link-format': 'yyyy-mm-dd'}))

    class Meta:
        model = Task
        fields = ('project_name', 'cp4', 'affect_app', 'branch', 'developer', 'submitdate', 'releasedate')

        # 简单方式
        # {#        <form action="{% url 'perf' %}" method="post" class="form-horizontal" >#}
        # {#            {% csrf_token %}#}
        # {#            {{ form }}#}
        # {#          <button type="submit" class="btn btn-default">Submit</button>#}
        # {#        </form>#}
