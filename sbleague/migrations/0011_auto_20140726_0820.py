# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0010_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='gameID',
            field=models.IntegerField(serialize=False, primary_key=True),
        ),
    ]
