# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-02-27 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_session_is_admission'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]