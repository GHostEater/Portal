# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-17 10:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20171002_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genotype',
            field=models.CharField(blank=True, choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('CS', 'CS'), ('AC', 'AC')], max_length=5, null=True),
        ),
    ]
