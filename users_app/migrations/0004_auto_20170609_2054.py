# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-09 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_auto_20170609_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.CharField(max_length=5, null=True, verbose_name='ZIP code'),
        ),
    ]
