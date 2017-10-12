# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-12 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0026_auto_20171012_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='utterance',
            name='media_end',
            field=models.FloatField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='utterance',
            name='media_start',
            field=models.FloatField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='utterance',
            name='media_unit',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
