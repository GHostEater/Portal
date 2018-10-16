# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_session_is_admission'),
        ('admission', '0004_remove_application_session'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='session',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='session.Session'),
            preserve_default=False,
        ),
    ]
