# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-10 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20170810_1411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='goods',
            field=models.ManyToManyField(blank=True, null=True, to='goods.GoodsList', verbose_name='\u5546\u54c1'),
        ),
    ]
