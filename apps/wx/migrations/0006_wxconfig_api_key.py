# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-01 13:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0005_wxconfig_mch_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='wxconfig',
            name='api_key',
            field=models.CharField(max_length=40, null=True, verbose_name='\u5546\u6237API\u5bc6\u94a5'),
        ),
    ]
