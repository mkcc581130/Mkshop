# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='area',
            old_name='areas',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='cities',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='province',
            old_name='provinces',
            new_name='name',
        ),
    ]
