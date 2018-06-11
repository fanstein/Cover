# coding=utf8
from django import forms


class Form1(forms.Form):
    user = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class':'form-control'}))
    pwd = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'password'}))


class Jmeter_F(forms.Form):
    api_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    threads = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    duration = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    host = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    port = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    method = forms.ChoiceField(widget=forms.TextInput(attrs={'class':'form-control'}))
    path = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    body_data = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))




    # class Meta:
    #     model = user
    #     field = ('post',)

#简单方式
# {#        <form action="{% url 'perf' %}" method="post" class="form-horizontal" >#}
# {#            {% csrf_token %}#}
# {#            {{ form }}#}
# {#          <button type="submit" class="btn btn-default">Submit</button>#}
# {#        </form>#}