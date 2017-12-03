# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-23 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0006_producto_logo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='app3',
            new_name='app_Android',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='app2',
            new_name='app_Mac',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='app1',
            new_name='app_Windows',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.AddField(
            model_name='producto',
            name='respos',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]