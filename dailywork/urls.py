from django.conf.urls import include, url
from views import *
from django.views.generic import TemplateView


urlpatterns = [
    # url(r'^$', index),
    url(r'^$', TemplateView.as_view(template_name='home.html'),name='home'),
    url(r'^notice/$', TemplateView.as_view(template_name='notice.html'),name='notice'),
    url(r'^learn/$', TemplateView.as_view(template_name='learn/div2.html')),
    url(r'^perf/$', perf, name='perf'),
    url(r'^task/', get_task, name='task'),
    url(r'^result/', get_perf_result, name='get_perf_result'),
    url(r'^deploy',deploy,name='deploy'),
    url(r'^daily/', daily_task, name='daily_task'),
    url(r'^viewtest/$', ServerListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', ServerDetailView.as_view(), name='detail'),
]