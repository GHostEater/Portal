# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-28 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0023_auto_20170927_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='cert1',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cert1_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cert2',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='cert2_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='comp_lit',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='degree',
            field=models.CharField(blank=True, choices=[('IJMB', 'IJMB'), ('JUPEB', 'JUPEB'), ('NCE', 'NCE'), ('ND', 'ND'), ('HND', 'HND')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='degree_class',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='duration',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='jamb_no',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='jamb_score',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='lga',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='marital_status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='mode_of_entry',
            field=models.CharField(blank=True, choices=[('UTME Candidate', 'UTME Candidate'), ('Transfer', 'Transfer'), ('Direct Entry', 'Direct Entry')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='nationality',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='next_kin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='next_kin_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='objection',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='offence',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='passport_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='pin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='programme',
            field=models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate'), ('JUPEB', 'JUPEB')], max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='programme_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Executive', 'Executive')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='referee_phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='religion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='residence',
            field=models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Off Campus', 'Off Campus')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='sex',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='sponsor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='sponsor_phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='state_of_origin',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='year_entry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
