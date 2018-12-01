# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-10 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0014_auto_20170909_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='type',
        ),
        migrations.AddField(
            model_name='application',
            name='mode_of_entry',
            field=models.CharField(blank=True, choices=[('UTME Candidate', 'UTME Candidate'), ('Transfer', 'Transfer'), ('Direct Entry', 'Direct Entry')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='programme_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], max_length=50),
        ),
    ]
