# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 06:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=datetime.datetime(2017, 5, 25, 6, 27, 7, 731585, tzinfo=utc))),
                ('photo', models.ImageField(upload_to='')),
            ],
        ),
    ]
