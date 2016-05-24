# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='description',
        ),
        migrations.AddField(
            model_name='room',
            name='img',
            field=models.CharField(default=0, max_length=50, verbose_name='照片路径'),
            preserve_default=False,
        ),
    ]
