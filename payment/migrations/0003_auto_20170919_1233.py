# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-19 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20170910_2059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paymentType',
            new_name='payment_type',
        ),
        migrations.AlterField(
            model_name='payment',
            name='rrr',
            field=models.TextField(),
        ),
    ]
