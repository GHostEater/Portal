# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-06 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymenttype', '0002_auto_20170925_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttype',
            name='private_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='paymenttype',
            name='public_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='api_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='merchant_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttype',
            name='service_type_id',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
