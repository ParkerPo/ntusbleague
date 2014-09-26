# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0008_pitching_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitching',
            name='h',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
