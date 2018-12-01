# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-05 11:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0001_initial'),
        ('paymentwaving', '0003_auto_20170919_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='wavedpayment',
            name='level',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='level.Level'),
            preserve_default=False,
        ),
    ]
