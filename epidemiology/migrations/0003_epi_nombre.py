# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-20 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epidemiology', '0002_auto_20160820_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='epi',
            name='nombre',
            field=models.CharField(default='Titulo predeterminado', max_length=24),
        ),
    ]