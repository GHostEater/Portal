# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-03-07 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sysinfo',
            name='portal_site',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
