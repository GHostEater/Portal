# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-13 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0016_auto_20170910_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='second_choice',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
