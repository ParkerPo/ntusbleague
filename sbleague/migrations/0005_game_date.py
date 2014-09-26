# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0004_auto_20140725_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.date(2014, 7, 25), blank=True),
            preserve_default=False,
        ),
    ]
