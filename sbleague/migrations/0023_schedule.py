# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbleague', '0022_auto_20140913_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('location', models.CharField(max_length=200)),
                ('away', models.ForeignKey(to='sbleague.Team')),
                ('home', models.ForeignKey(to='sbleague.Team')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
