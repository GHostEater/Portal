# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-08 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0012_auto_20170908_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='dateBirth',
            field=models.DateTimeField(),
        ),
    ]
