# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-25 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0002_application_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
