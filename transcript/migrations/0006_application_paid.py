# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-04-23 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0005_auto_20190307_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
