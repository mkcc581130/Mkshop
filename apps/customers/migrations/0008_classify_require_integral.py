# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 16:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20170809_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='classify',
            name='require_integral',
            field=models.IntegerField(default=0, verbose_name='\u9700\u6c42\u79ef\u5206'),
        ),
    ]
