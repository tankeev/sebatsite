# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 20:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20170814_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 20, 22, 4, 953047, tzinfo=utc)),
        ),
    ]