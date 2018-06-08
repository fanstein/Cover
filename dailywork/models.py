# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CatServerInfo(models.Model):
    id = models.AutoField(primary_key=True)
    app_id = models.IntegerField(unique=True)
    # name = models.CharField(max_length=100, blank=True, null=True)
    # chinese_name = models.CharField(max_length=50, blank=True, null=True)
    # appimportance = models.CharField(max_length=5, blank=True, null=True)
    # appcontainer = models.CharField(max_length=20, blank=True, null=True)
    # owner = models.CharField(max_length=100, blank=True, null=True)
    # status = models.CharField(max_length=10, blank=True, null=True)
    # group = models.CharField(max_length=100, blank=True, null=True)
    # group_id = models.IntegerField(blank=True, null=True)
    # owner_name = models.CharField(max_length=10, blank=True, null=True)
    # update_time = models.DateTimeField(blank=True, null=True)
    # svr = models.CharField(max_length=255, blank=True, null=True)
    # appcategory = models.CharField(max_length=255, blank=True, null=True)
    # appcreatetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_server_info'