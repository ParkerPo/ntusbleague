# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0007_auto_20140726_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitching',
            name='ip',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
