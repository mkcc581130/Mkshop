# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-23 15:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Verify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tel', models.CharField(max_length=12, verbose_name='\u624b\u673a\u53f7')),
                ('code', models.CharField(max_length=8, verbose_name='\u9a8c\u8bc1\u7801')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='\u751f\u6210\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u9a8c\u8bc1\u7801',
                'verbose_name_plural': '\u9a8c\u8bc1\u7801\u5217\u8868',
            },
        ),
    ]