# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-28 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0061_withdraworders'),
    ]

    operations = [
        migrations.AddField(
            model_name='withdraworders',
            name='name',
            field=models.CharField(max_length=16, null=True, verbose_name='\u59d3\u540d'),
        ),
        migrations.AlterField(
            model_name='withdraworders',
            name='handing_time',
            field=models.DateTimeField(null=True, verbose_name='\u5904\u7406\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='withdraworders',
            name='oid',
            field=models.CharField(max_length=16, null=True, verbose_name='\u8ba2\u5355\u7f16\u53f7'),
        ),
        migrations.AlterField(
            model_name='withdraworders',
            name='status',
            field=models.IntegerField(choices=[(0, '\u672a\u5904\u7406'), (1, '\u5df2\u5904\u7406')], default=0, verbose_name='\u63d0\u73b0\u72b6\u6001'),
        ),
    ]