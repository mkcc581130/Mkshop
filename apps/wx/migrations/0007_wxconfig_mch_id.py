# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-01 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0006_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='wxconfig',
            name='mch_id',
            field=models.CharField(max_length=40, null=True, verbose_name='\u5546\u6237ID'),
        ),
    ]