# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0003_auto_20160503_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='applicant_department',
        ),
        migrations.AddField(
            model_name='reservation',
            name='applicant_department',
            field=models.ForeignKey(verbose_name='申请人学院', to='SUTCM_RR_db.Department', default=0),
            preserve_default=False,
        ),
    ]
