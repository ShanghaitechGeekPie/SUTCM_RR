# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0002_auto_20160511_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='sn',
            field=models.CharField(unique=True, max_length=6, verbose_name='查询代码'),
        ),
    ]
