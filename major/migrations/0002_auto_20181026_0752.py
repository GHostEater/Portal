# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-26 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='major',
            name='degree',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='major',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
