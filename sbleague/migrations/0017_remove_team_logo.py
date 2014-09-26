# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0016_auto_20140728_1403'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='logo',
        ),
    ]
