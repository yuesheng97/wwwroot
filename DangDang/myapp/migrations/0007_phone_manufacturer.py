# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-17 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20181016_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='manufacturer',
            field=models.CharField(default='', max_length=8),
        ),
    ]
