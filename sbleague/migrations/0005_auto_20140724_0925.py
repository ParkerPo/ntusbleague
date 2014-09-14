# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0004_auto_20140724_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='scorebox',
            field=models.CharField(max_length=200),
        ),
    ]
