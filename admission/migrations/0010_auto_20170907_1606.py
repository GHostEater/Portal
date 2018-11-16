# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('level', '0001_initial'),
        ('admission', '0009_auto_20170907_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='degree',
            field=models.CharField(blank=True, choices=[('IJMB', 'IJMB'), ('JUPEB', 'JUPEB'), ('NCE', 'NCE'), ('ND', 'ND'), ('HND', 'HND')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='level.Level'),
        ),
        migrations.AlterField(
            model_name='application',
            name='cert1',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cert2',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=20, null=True),
        ),
    ]