# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-09 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='credit',
            field=models.CharField(default='8', max_length=3),
        ),
    ]
