# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-06-28 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_payment_transcript_app'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='narration',
            field=models.TextField(blank=True, null=True),
        ),
    ]