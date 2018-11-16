# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-07 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0062_auto_20180328_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='received_packet',
            field=models.BooleanField(default=False, verbose_name='\u662f\u5426\u9886\u53d6\u7ea2\u5305'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, '\u5f85\u4ed8\u6b3e'), (1, '\u5df2\u652f\u4ed8'), (2, '\u5f85\u53d1\u8d27'), (3, '\u5df2\u53d1\u8d27'), (4, '\u5df2\u5b8c\u6210'), (5, '\u5df2\u5173\u95ed'), (6, '\u9000\u6b3e\u4e2d')], verbose_name='\u8ba2\u5355\u72b6\u6001'),
        ),
    ]