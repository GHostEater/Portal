# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-07 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_student_programme_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='olevel',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('WAEC/GCE', 'WAEC/GCE'), ('NECO/GCE', 'NECO/GCE'), ('WAEC/NECO', 'WAEC/NECO'), ('NABTEB', 'NABTEB')], max_length=15, null=True),
        ),
    ]
