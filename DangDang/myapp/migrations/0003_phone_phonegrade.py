# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-09 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_user_credit'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='phoneGrade',
            field=models.CharField(default='9', max_length=3),
        ),
    ]
