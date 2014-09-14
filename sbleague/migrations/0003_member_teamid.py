# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0002_auto_20140720_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='teamID',
            field=models.ForeignKey(default=0, to='sbleague.Team'),
            preserve_default=False,
        ),
    ]
