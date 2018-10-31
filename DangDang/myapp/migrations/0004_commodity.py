# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-16 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_phone_phonegrade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('phonenum', models.IntegerField(primary_key=True, serialize=False)),
                ('phoneModel', models.CharField(max_length=5)),
                ('phonePrice', models.CharField(max_length=15)),
                ('phoneCharacter', models.CharField(max_length=10)),
            ],
        ),
    ]
