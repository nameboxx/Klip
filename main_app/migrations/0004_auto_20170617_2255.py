# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 22:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20170617_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='date_expires',
            field=models.DateField(default=datetime.datetime(2017, 7, 17, 22, 55, 50, 938996)),
        ),
    ]