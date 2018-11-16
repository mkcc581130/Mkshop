# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-07 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0027_auto_20180404_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='discount',
        ),
        migrations.AddField(
            model_name='coupon',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='goods/coupon/', verbose_name='\u56fe\u7247'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='is_auto',
            field=models.BooleanField(default=True, verbose_name='\u662f\u5426\u81ea\u52a8\u9886\u53d6'),
        ),
    ]
