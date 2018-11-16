# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-14 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('major', '0002_auto_20181023_0736'),
        ('paymenttype', '0008_auto_20181114_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tuitionfee',
            name='dept',
        ),
        migrations.AddField(
            model_name='tuitionfee',
            name='major',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='major.Major'),
            preserve_default=False,
        ),
    ]
