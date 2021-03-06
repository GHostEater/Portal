# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-24 07:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0019_auto_20170919_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='additional_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='appointments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='current_course',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='disability',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='honours',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='institution_attended',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='maiden_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='marital_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='next_kin',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='next_kin_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='next_kin_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='nysc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='nysc_img',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AddField(
            model_name='application',
            name='objection',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='passport_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='post_address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='publications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='residence',
            field=models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Off Campus', 'Off Campus')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='transcript',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='year_entry',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='comp_lit',
            field=models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='extracurricular',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='first_choice',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='offence',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='programme_type',
            field=models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Executive', 'Executive')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='referee',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='second_choice',
            field=models.TextField(blank=True, null=True),
        ),
    ]
