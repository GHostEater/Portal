# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-09-07 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0029_auto_20180728_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='dean_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='dean_signature',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='application',
            name='hod_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='hod_signature',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]