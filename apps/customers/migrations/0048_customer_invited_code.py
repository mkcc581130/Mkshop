# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-15 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0047_auto_20180315_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='invited_code',
            field=models.IntegerField(blank=True, null=True, verbose_name='\u88ab\u9080\u8bf7\u7801'),
        ),
    ]