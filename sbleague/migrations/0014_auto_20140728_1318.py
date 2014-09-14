# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0013_pitching_outs'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitching',
            name='sequence',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pitching',
            name='ip',
        ),
    ]
