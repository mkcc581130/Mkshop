# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-01 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0038_auto_20171101_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='prepay_id',
        ),
        migrations.AddField(
            model_name='order',
            name='pay_oid',
            field=models.CharField(max_length=40, null=True, verbose_name='\u652f\u4ed8\u8ba2\u5355\u53f7'),
        ),
    ]
