# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20170906_1344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='modeofentry',
            new_name='modeOfEntry',
        ),
    ]