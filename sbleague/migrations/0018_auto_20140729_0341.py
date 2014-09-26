# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0017_remove_team_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='currnet',
            field=models.BooleanField(default=True),
        ),
    ]
