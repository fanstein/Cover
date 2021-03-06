# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-06-13 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatServerInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('app_id', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'cat_server_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JmeterRuntime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('api_name', models.CharField(blank=True, max_length=100, null=True)),
                ('threads', models.CharField(blank=True, max_length=100, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('host', models.CharField(blank=True, max_length=100, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('method', models.CharField(blank=True, max_length=100, null=True)),
                ('path', models.CharField(blank=True, max_length=100, null=True)),
                ('body_data', models.CharField(blank=True, max_length=255, null=True)),
                ('change_lasttime', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jmeter_runtime',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=255, null=True)),
                ('affect_app', models.CharField(blank=True, max_length=255, null=True)),
                ('branch', models.CharField(blank=True, max_length=255, null=True)),
                ('developer', models.CharField(blank=True, max_length=255, null=True)),
                ('submitdate', models.DateField(blank=True, null=True)),
                ('is_finish', models.BooleanField(default=False)),
                ('releasedate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
