# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0025_auto_20140926_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='teamID',
            field=models.AutoField(default=(1, 2, 3, 4, 5, 6), serialize=False, primary_key=True),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='team',
            name='id',
        ),
    ]
