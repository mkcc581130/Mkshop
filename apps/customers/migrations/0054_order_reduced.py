# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-19 22:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0053_auto_20180318_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reduced',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='\u5df2\u4f18\u60e0'),
        ),
    ]
