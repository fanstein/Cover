# coding=utf8
from django import forms
from models import *

Method_Choice = (
    ('1', 'GET'),
    ('2', 'POST'),
    ('3', 'PUT'),
)


class Form1(forms.Form):
    user = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'password'}))


class Jmeter_F(forms.Form):
    api_name = forms.CharField(label='接口名',widget=forms.TextInput(attrs={'class':'form-control'}))
    threads = forms.CharField(initial=10,label='线程数',widget=forms.TextInput(attrs={'class':'form-control'}))
    duration = forms.IntegerField(initial=600,label='执行时长',widget=forms.TextInput(attrs={'class':'form-control'}))
    host = forms.CharField(label='服务器地址',widget=forms.TextInput(attrs={'class':'form-control'}))
    port = forms.IntegerField(initial=80,label='端口',widget=forms.TextInput(attrs={'class':'form-control'}))
    method = forms.ChoiceField(choices=Method_Choice,label='方法',widget=forms.Select(attrs={'class':'form-control'}))
    path = forms.CharField(label='路径',widget=forms.TextInput(attrs={'class':'form-control'}))
    body_data = forms.CharField(label='报文',widget=forms.Textarea(attrs={'class':'form-control'}))

    class Meta:
        model = JmeterRuntime
        field = ('post',)


class task_F(forms.Form):
    project_name = forms.CharField(label='项目名', widget=forms.TextInput(attrs={'class':'form-control'}))
    affect_app = forms.CharField(label='影响app', widget=forms.TextInput(attrs={'class':'form-control'}))
    branch = forms.CharField(label='分支', widget=forms.TextInput(attrs={'class':'form-control'}))
    developer = forms.CharField(label='开发', widget=forms.TextInput(attrs={'class':'form-control'}))
    submitdate = forms.DateTimeField(label='提测日期', widget=forms.DateTimeInput(attrs={'class':'form-control'}))
    releasedate = forms.DateTimeField(label='发布日期', widget=forms.DateTimeInput(attrs={'class':'form-control'}))

#简单方式
# {#        <form action="{% url 'perf' %}" method="post" class="form-horizontal" >#}
# {#            {% csrf_token %}#}
# {#            {{ form }}#}
# {#          <button type="submit" class="btn btn-default">Submit</button>#}
# {#        </form>#}