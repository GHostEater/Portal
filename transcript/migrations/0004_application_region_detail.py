# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-28 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0003_auto_20180726_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='region_detail',
            field=models.TextField(blank=True, choices=[('Africa', 'Africa'), ('North America', 'North America'), ('South America', 'South America'), ('Europe', 'Europe'), ('Asia', 'Asia'), ('Oceania', 'Oceania')], null=True),
        ),
    ]
