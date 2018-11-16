# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-30 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0035_auto_20171017_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='WxOauth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5fae\u4fe1OpenID')),
                ('access_token', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5fae\u4fe1ACCESS_TOKEN')),
                ('refresh_token', models.CharField(blank=True, max_length=50, null=True, verbose_name='\u5fae\u4fe1REFRESH_TOKEN')),
            ],
            options={
                'verbose_name': '\u5fae\u4fe1\u767b\u5f55\u4fe1\u606f',
                'verbose_name_plural': '\u5fae\u4fe1\u767b\u5f55\u4fe1\u606f\u5217\u8868',
            },
        ),
        migrations.AlterField(
            model_name='customer',
            name='tel',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AddField(
            model_name='wxoauth',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer', verbose_name='\u7528\u6237'),
        ),
    ]
