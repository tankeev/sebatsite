# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-23 15:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170720_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 23, 15, 29, 24, 949647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.FileField(blank=True, default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
    ]