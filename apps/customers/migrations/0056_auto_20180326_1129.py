# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-26 11:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0055_auto_20180323_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankBin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=30, null=True, verbose_name='\u94f6\u884c')),
                ('bin', models.CharField(max_length=16, null=True, verbose_name='\u8ba2\u5355\u7f16\u53f7')),
            ],
        ),
        migrations.CreateModel(
            name='UnableCommission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commission', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='\u672a\u7ed3\u7b97\u4f63\u91d1')),
                ('is_settled', models.BooleanField(default=False, verbose_name='\u662f\u5426\u7ed3\u7b97')),
                ('settled_time', models.DateTimeField(blank=True, null=True, verbose_name='\u7ed3\u7b97\u65f6\u95f4')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Order', verbose_name='\u6240\u5c5e\u8ba2\u5355')),
            ],
            options={
                'verbose_name': '\u672a\u7ed3\u7b97\u4f63\u91d1',
                'verbose_name_plural': '\u672a\u7ed3\u7b97\u4f63\u91d1\u5217\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='remindorders',
            options={'verbose_name': '\u63d0\u9192\u53d1\u8d27', 'verbose_name_plural': '\u63d0\u9192\u53d1\u8d27\u5217\u8868'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='\u603b\u4f63\u91d1'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='enable_commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='\u53ef\u63d0\u73b0\u4f63\u91d1'),
        ),
        migrations.AlterField(
            model_name='remindorders',
            name='remind_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u63d0\u9192\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='withdraworders',
            name='withdraw_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u63d0\u73b0\u65f6\u95f4'),
        ),
        migrations.AddField(
            model_name='unablecommission',
            name='spokesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='\u63a8\u5e7f\u4eba'),
        ),
    ]