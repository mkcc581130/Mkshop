# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-09 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20170809_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default', models.BooleanField(verbose_name='\u9ed8\u8ba4\u5730\u5740')),
                ('areas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Area', verbose_name='\u533a')),
                ('cities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.City', verbose_name='\u5e02')),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='\u5ba2\u6237')),
                ('provinces', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Province', verbose_name='\u7701')),
            ],
            options={
                'verbose_name': '\u6536\u8d27\u5730\u5740\u5217\u8868',
                'verbose_name_plural': '\u6536\u8d27\u5730\u5740\u5217\u8868',
            },
        ),
    ]