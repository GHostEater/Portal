# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170613_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Academic Affairs'), ('3', 'Bursar'), ('4', 'Student Affairs'), ('5', 'College Officer'), ('6', 'Lecturer'), ('7', 'Student')], default='', max_length=2),
        ),
    ]
