# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.IntegerField(choices=[('1', '1st Semester'), ('2', '2nd Semester')], default=0),
        ),
    ]
