# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0005_game_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitching',
            name='h',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pitching',
            name='ip',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
