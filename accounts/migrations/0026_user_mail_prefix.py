# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-12-06 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0025_user_sign'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='mail_prefix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]