# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0024_member_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=3, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='team',
            name='teamID',
        ),
    ]
