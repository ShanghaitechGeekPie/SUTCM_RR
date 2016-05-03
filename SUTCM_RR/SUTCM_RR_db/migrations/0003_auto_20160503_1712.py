# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0002_auto_20160503_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '用途种类', 'verbose_name_plural': '用途种类'},
        ),
        migrations.AddField(
            model_name='reservation',
            name='people',
            field=models.PositiveSmallIntegerField(verbose_name='使用人数', default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(verbose_name='预约用途', max_length=10),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(verbose_name='院系/专业名称', max_length=50),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='category',
            field=models.ForeignKey(verbose_name='预约种类', to='SUTCM_RR_db.Category'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='purpose',
            field=models.TextField(verbose_name='具体申请用途', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='available_for',
            field=models.ManyToManyField(to='SUTCM_RR_db.Category', verbose_name='可预约用途'),
        ),
        migrations.AlterField(
            model_name='room',
            name='capacity',
            field=models.PositiveSmallIntegerField(verbose_name='最大承载人数'),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(verbose_name='房间名称', max_length=20),
        ),
    ]
