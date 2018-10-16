# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-09 07:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hostel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('size', models.IntegerField()),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hostel.Hostel')),
            ],
        ),
    ]
