# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SUTCM_RR_db', '0004_auto_20160503_1829'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name_plural': '房间', 'verbose_name': '房间'},
        ),
        migrations.RenameField(
            model_name='room',
            old_name='available_for',
            new_name='category',
        ),
    ]
