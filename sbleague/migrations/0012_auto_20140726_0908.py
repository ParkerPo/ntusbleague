# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0011_auto_20140726_0820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='batting',
            old_name='gameID',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='batting',
            old_name='memberID',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='batting',
            old_name='teamID',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='awayID',
            new_name='away',
        ),
        migrations.RenameField(
            model_name='game',
            old_name='homeID',
            new_name='home',
        ),
        migrations.RenameField(
            model_name='member',
            old_name='teamID',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='pitching',
            old_name='gameID',
            new_name='game',
        ),
        migrations.RenameField(
            model_name='pitching',
            old_name='memberID',
            new_name='member',
        ),
        migrations.RenameField(
            model_name='pitching',
            old_name='teamID',
            new_name='team',
        ),
    ]
