# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_commodity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='phoneCharacter',
            field=models.CharField(default=None, max_length=10),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='phoneModel',
            field=models.CharField(default=None, max_length=5),
        ),
        migrations.AlterField(
            model_name='commodity',
            name='phonePrice',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
