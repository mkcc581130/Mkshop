# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-04 15:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0025_auto_20170901_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergoods',
            name='image',
        ),
    ]