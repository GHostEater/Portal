# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-25 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_payment_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='rrr',
            field=models.TextField(blank=True, null=True),
        ),
    ]
