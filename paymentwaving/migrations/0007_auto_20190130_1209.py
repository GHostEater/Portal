# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-30 11:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paymentwaving', '0006_auto_20181114_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wavedpayment',
            name='waved_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
