# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 19:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paymenttype',
            new_name='paymentType',
        ),
    ]