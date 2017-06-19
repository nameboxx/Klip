# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 23:33
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dispensary',
            options={'verbose_name_plural': 'dispensaries'},
        ),
        migrations.AlterField(
            model_name='deal',
            name='date_expires',
            field=models.DateField(default=datetime.datetime(2017, 7, 16, 23, 33, 2, 155684)),
        ),
        migrations.AddField(
            model_name='review',
            name='deal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='main_app.Deal'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]