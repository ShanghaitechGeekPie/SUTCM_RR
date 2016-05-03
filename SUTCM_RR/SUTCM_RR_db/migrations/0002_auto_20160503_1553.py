# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=10, verbose_name='资源类型名')),
            ],
            options={
                'verbose_name_plural': '资源类型',
                'verbose_name': '资源类型',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='学院名称')),
            ],
            options={
                'verbose_name_plural': '院系/专业',
                'verbose_name': '院系/专业',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=20, verbose_name='资源名称')),
                ('location', models.CharField(max_length=20, verbose_name='位置')),
                ('capacity', models.PositiveSmallIntegerField(verbose_name='最大容纳人数')),
                ('description', models.TextField(blank=True, verbose_name='简介')),
                ('provider_name', models.CharField(max_length=20, verbose_name='负责人')),
                ('open_hours', models.CharField(max_length=50, verbose_name='开放时间')),
                ('available_for', models.ManyToManyField(verbose_name='可预约类型', to='SUTCM_RR_db.Category')),
            ],
            options={
                'verbose_name_plural': '资源',
                'verbose_name': '资源',
            },
        ),
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name_plural': '预约', 'verbose_name': '预约'},
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='applicant_department',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.NullBooleanField(default=None, verbose_name='申请通过状态'),
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
        migrations.AddField(
            model_name='reservation',
            name='category',
            field=models.ForeignKey(verbose_name='预约类型', default=0, to='SUTCM_RR_db.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(verbose_name='申请房间', default=1, to='SUTCM_RR_db.Room'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='applicant_department',
            field=models.ManyToManyField(verbose_name='申请人学院', to='SUTCM_RR_db.Department'),
        ),
    ]
