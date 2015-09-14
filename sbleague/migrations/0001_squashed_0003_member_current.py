# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'sbleague', '0001_initial'), (b'sbleague', '0002_remove_member_current'), (b'sbleague', '0003_member_current')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField()),
                ('pa', models.IntegerField()),
                ('single', models.IntegerField()),
                ('double', models.IntegerField()),
                ('triple', models.IntegerField()),
                ('hr', models.IntegerField()),
                ('rbi', models.IntegerField()),
                ('run', models.IntegerField()),
                ('bb', models.IntegerField()),
                ('so', models.IntegerField()),
                ('sf', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('gameID', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('location', models.CharField(max_length=200)),
                ('scorebox', models.CharField(max_length=200, blank=True)),
                ('away_R', models.IntegerField()),
                ('away_H', models.IntegerField()),
                ('away_E', models.IntegerField()),
                ('home_R', models.IntegerField()),
                ('home_H', models.IntegerField()),
                ('home_E', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='batting',
            name='game',
            field=models.ForeignKey(to='sbleague.Game'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberID', models.AutoField(serialize=False, primary_key=True)),
                ('current', models.IntegerField(max_length=1)),
                ('name', models.CharField(max_length=50)),
                ('studentID', models.CharField(max_length=9)),
                ('number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='batting',
            name='member',
            field=models.ForeignKey(to='sbleague.Member'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sequence', models.IntegerField()),
                ('outs', models.IntegerField()),
                ('pa', models.IntegerField()),
                ('h', models.IntegerField()),
                ('hr', models.IntegerField()),
                ('bb', models.IntegerField()),
                ('so', models.IntegerField()),
                ('r', models.IntegerField()),
                ('er', models.IntegerField()),
                ('go', models.IntegerField()),
                ('fo', models.IntegerField()),
                ('win', models.IntegerField()),
                ('lose', models.IntegerField()),
                ('game', models.ForeignKey(to='sbleague.Game')),
                ('member', models.ForeignKey(to='sbleague.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(blank=True)),
                ('time', models.TimeField(blank=True)),
                ('location', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('teamID', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('current', models.IntegerField(max_length=1, choices=[(0, b'\xe4\xb8\x8d\xe5\xad\x98\xe5\x9c\xa8'), (1, b'\xe4\xb8\x81\xe4\xb8\x81\xe8\x81\xaf\xe7\x9b\x9f'), (2, b'\xe6\x8b\x89\xe6\x8b\x89\xe8\x81\xaf\xe7\x9b\x9f')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='schedule',
            name='home',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='schedule',
            name='away',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pitching',
            name='team',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='team',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='home',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='away',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batting',
            name='team',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='member',
            name='current',
        ),
        migrations.AddField(
            model_name='member',
            name='current',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=False,
        ),
    ]
