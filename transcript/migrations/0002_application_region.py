# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-23 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='region',
            field=models.TextField(choices=[('Local', 'Local'), ('Foreign', 'Foreign')], default='Local'),
        ),
    ]
