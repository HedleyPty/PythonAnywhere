# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_auto_20160223_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='app_Mac',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='app_Windows',
        ),
        migrations.AddField(
            model_name='producto',
            name='app',
            field=models.CharField(default=b'URL del app', max_length=200),
        ),
    ]
