from django.conf.urls import include, url
from views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', index),
    url(r'^test/$', TemplateView.as_view(template_name='bootstrap_base_2.html')),
    url(r'^perf/$', perf, name='perf'),
    url(r'^viewtest/$', ServerListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', ServerDetailView.as_view(), name='detail'),
]