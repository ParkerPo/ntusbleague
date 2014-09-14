# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0019_auto_20140729_0356'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score_tmp',
            field=models.CommaSeparatedIntegerField(default=0, max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='team',
            name='current',
            field=models.IntegerField(max_length=1, choices=[(0, b'\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8'), (1, b'\xe4\xb8\x81\xe4\xb8\x81\xe8\x81\xaf\xe7\x9b\x9f'), (2, b'\xe6\x8b\x89\xe6\x8b\x89\xe8\x81\xaf\xe7\x9b\x9f')]),
        ),
    ]
