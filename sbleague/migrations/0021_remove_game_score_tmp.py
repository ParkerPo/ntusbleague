# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0020_auto_20140912_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='score_tmp',
        ),
    ]
