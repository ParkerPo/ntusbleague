# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0012_auto_20140726_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='pitching',
            name='outs',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
