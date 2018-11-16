# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-10 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0022_auto_20171009_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifyone',
            name='en_name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='classifytwo',
            name='en_name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='detailprops',
            name='en_name',
            field=models.CharField(default='', max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='goodslist',
            name='en_name',
            field=models.CharField(max_length=100, verbose_name='Goods Name'),
        ),
        migrations.AlterField(
            model_name='props',
            name='en_name',
            field=models.CharField(default='', max_length=40, verbose_name='Name'),
        ),
    ]
