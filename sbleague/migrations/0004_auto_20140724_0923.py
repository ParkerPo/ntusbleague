# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0003_member_teamid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='location',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='game',
            name='scorebox',
            field=models.IntegerField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='studentID',
            field=models.CharField(max_length=9),
        ),
    ]
