# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-15 19:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20170815_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 19, 12, 45, 333868, tzinfo=utc)),
        ),
    ]
