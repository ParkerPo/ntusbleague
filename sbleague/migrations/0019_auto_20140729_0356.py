# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0018_auto_20140729_0341'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='currnet',
            new_name='current',
        ),
    ]
