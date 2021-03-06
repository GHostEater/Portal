# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-01-30 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SysInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('short_name', models.CharField(max_length=256)),
                ('med_name', models.CharField(max_length=256)),
                ('long_name', models.CharField(max_length=256)),
                ('slogan', models.CharField(max_length=256)),
                ('receipt_name', models.CharField(max_length=256)),
                ('site', models.CharField(max_length=256)),
                ('result_email', models.CharField(max_length=256)),
                ('noreply_email', models.CharField(max_length=256)),
            ],
        ),
    ]
