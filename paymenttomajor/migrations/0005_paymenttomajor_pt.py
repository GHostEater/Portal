# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-01 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymenttomajor', '0004_auto_20180321_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttomajor',
            name='pt',
            field=models.BooleanField(default=False),
        ),
    ]
