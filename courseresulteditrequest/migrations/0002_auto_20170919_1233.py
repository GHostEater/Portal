# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-19 11:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseresulteditrequest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='editedBy',
            new_name='edited_by',
        ),
        migrations.RenameField(
            model_name='request',
            old_name='handledBy',
            new_name='handled_by',
        ),
    ]
