# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gameID', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=10)),
                ('scorebox', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='batting',
            name='gameID',
            field=models.ForeignKey(to='sbleague.Game'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memberID', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('studentID', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='batting',
            name='memberID',
            field=models.ForeignKey(to='sbleague.Member'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Pitching',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pa', models.IntegerField()),
                ('so', models.IntegerField()),
                ('bb', models.IntegerField()),
                ('hr', models.IntegerField()),
                ('r', models.IntegerField()),
                ('er', models.IntegerField()),
                ('go', models.IntegerField()),
                ('fo', models.IntegerField()),
                ('win', models.IntegerField()),
                ('lose', models.IntegerField()),
                ('gameID', models.ForeignKey(to='sbleague.Game')),
                ('memberID', models.ForeignKey(to='sbleague.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teamID', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('currnet', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='pitching',
            name='teamID',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='homeID',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='game',
            name='awayID',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='batting',
            name='teamID',
            field=models.ForeignKey(to='sbleague.Team'),
            preserve_default=True,
        ),
    ]
