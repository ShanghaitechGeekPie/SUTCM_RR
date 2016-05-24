# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='预约用途', max_length=10)),
            ],
            options={
                'verbose_name': '用途种类',
                'verbose_name_plural': '用途种类',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='院系/专业名称', max_length=50)),
            ],
            options={
                'verbose_name': '院系/专业',
                'verbose_name_plural': '院系/专业',
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('applicant_phone', models.BigIntegerField(verbose_name='申请人手机号', unique=True)),
                ('applicant_name', models.CharField(verbose_name='申请人姓名', max_length=30)),
                ('applicant_sid', models.PositiveSmallIntegerField(verbose_name='申请人学号')),
                ('status', models.NullBooleanField(verbose_name='申请通过状态', default=None)),
                ('people', models.PositiveSmallIntegerField(verbose_name='使用人数')),
                ('purpose', models.TextField(verbose_name='具体申请用途', max_length=50, blank=True)),
                ('time_begin', models.DateTimeField(verbose_name='开始时间')),
                ('time_end', models.DateTimeField(verbose_name='结束时间')),
                ('sn', models.CharField(verbose_name='查询代码', unique=True, max_length=5)),
                ('applicant_department', models.ForeignKey(verbose_name='申请人学院', to='SUTCM_RR_db.Department')),
                ('category', models.ForeignKey(verbose_name='预约种类', to='SUTCM_RR_db.Category')),
            ],
            options={
                'verbose_name': '预约',
                'verbose_name_plural': '预约',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='房间名称', max_length=20)),
                ('location', models.CharField(verbose_name='位置', max_length=20)),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='最大承载人数')),
                ('description', models.TextField(verbose_name='简介', blank=True)),
                ('provider_name', models.CharField(verbose_name='负责人', max_length=20)),
                ('open_hours', models.CharField(verbose_name='开放时间', max_length=50)),
                ('category', models.ManyToManyField(verbose_name='可预约用途', to='SUTCM_RR_db.Category')),
            ],
            options={
                'verbose_name': '房间',
                'verbose_name_plural': '房间',
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(verbose_name='申请房间', to='SUTCM_RR_db.Room'),
        ),
    ]
