# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='detail',
            field=models.TextField(default='', verbose_name='\u8be6\u7ec6\u5730\u5740'),
        ),
    ]
