# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-16 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20170916_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('1', 'Admin'), ('2', 'Academic Affairs'), ('3', 'Bursar'), ('4', 'Student Affairs'), ('5', 'College Officer'), ('6', 'Lecturer'), ('7', 'Student'), ('8', 'Dean'), ('9', 'Non-Academic Staff')], default='', max_length=2),
        ),
    ]
