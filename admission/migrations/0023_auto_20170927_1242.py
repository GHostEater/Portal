# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-27 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0022_application_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
