# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-02 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20170718_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[('Compulsory', 'Compulsory'), ('Elective', 'Elective'), ('Required', 'Required')], max_length=20),
        ),
    ]