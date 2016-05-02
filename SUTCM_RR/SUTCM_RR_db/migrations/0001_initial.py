# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('applicant_phone', models.BigIntegerField(verbose_name='申请人手机号', unique=True)),
                ('applicant_name', models.CharField(verbose_name='申请人姓名', max_length=30)),
                ('applicant_department', models.PositiveSmallIntegerField(verbose_name='申请人学院', choices=[(0, 'A学院'), (1, 'B学院')])),
                ('applicant_sid', models.PositiveSmallIntegerField(verbose_name='申请人学号')),
                ('status', models.NullBooleanField(default=None)),
                ('purpose', models.TextField(verbose_name='申请用途', blank=True, max_length=50)),
                ('time_begin', models.DateTimeField(verbose_name='开始时间')),
                ('time_end', models.DateTimeField(verbose_name='结束时间')),
                ('sn', models.CharField(verbose_name='查询代码', max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('category', models.PositiveSmallIntegerField(verbose_name='种类', choices=[(0, '活动室'), ('咨询', ((1, '创业'), (2, '就业'), (3, '心理')))])),
                ('name', models.CharField(verbose_name='资源名称', max_length=20)),
                ('location', models.CharField(verbose_name='位置', max_length=20)),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='最大容纳人数')),
                ('description', models.TextField(verbose_name='简介', blank=True)),
                ('provider_name', models.CharField(verbose_name='负责人', max_length=20)),
                ('open_hours', models.CharField(verbose_name='开放时间', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='resource',
            field=models.ForeignKey(to='SUTCM_RR_db.Resource'),
        ),
    ]
