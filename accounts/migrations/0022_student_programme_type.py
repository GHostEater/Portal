# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-01 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_student_parent_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='programme_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Executive', 'Executive')], default='Full Time', max_length=15),
        ),
    ]
