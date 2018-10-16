# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courseallocation', '0002_remove_courseallocation_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseallocation',
            name='position',
        ),
        migrations.AddField(
            model_name='courseallocation',
            name='assisting',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='courseallocation',
            name='coordinator',
            field=models.BooleanField(default=0),
        ),
    ]
