# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-25 06:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20170620_0659'),
    ]

    operations = [
        migrations.AddField(
            model_name='utterance',
            name='corpus',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='db.Corpus'),
        ),
        migrations.AddField(
            model_name='utterance',
            name='gloss',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='utterance',
            name='length',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='corpus',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 25, 6, 33, 36, 472603), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='transcript',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2017, 6, 25, 6, 33, 36, 474409), max_length=255, null=True),
        ),
    ]
