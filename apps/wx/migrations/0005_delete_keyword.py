# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-25 20:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0004_auto_20171025_2032'),
    ]

    operations = [
        migrations.DeleteModel(
            name='KeyWord',
        ),
    ]