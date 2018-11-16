# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-17 23:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0050_auto_20180317_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='enable_commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='\u4f63\u91d1'),
        ),
        migrations.AddField(
            model_name='customer',
            name='number_of_invited',
            field=models.IntegerField(default=0, verbose_name='\u7d2f\u8ba1\u9080\u8bf7'),
        ),
        migrations.AddField(
            model_name='customer',
            name='promote_order',
            field=models.IntegerField(default=0, verbose_name='\u63a8\u5e7f\u8ba2\u5355'),
        ),
    ]