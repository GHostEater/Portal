# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-08 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('major', '0001_initial'),
        ('session', '0001_initial'),
        ('level', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_no', models.CharField(blank=True, max_length=256, null=True)),
                ('programme', models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Undergraduate Transfer', 'Undergraduate Transfer'), ('Postgraduate', 'Postgraduate'), ('JUPEB', 'JUPEB')], max_length=200)),
                ('programme_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Executive', 'Executive')], max_length=200, null=True)),
                ('mode_of_entry', models.CharField(blank=True, choices=[('UTME Candidate', 'UTME Candidate'), ('Transfer', 'Transfer'), ('Direct Entry', 'Direct Entry')], max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('date_birth', models.DateField()),
                ('sex', models.CharField(max_length=200)),
                ('nationality', models.CharField(max_length=200)),
                ('state_of_origin', models.CharField(max_length=200)),
                ('lga', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=200)),
                ('religion', models.CharField(max_length=200)),
                ('sponsor', models.TextField()),
                ('sponsor_address', models.TextField()),
                ('sponsor_phone', models.CharField(max_length=200)),
                ('maiden_name', models.TextField(blank=True, null=True)),
                ('marital_status', models.CharField(blank=True, max_length=200, null=True)),
                ('passport_number', models.CharField(blank=True, max_length=200, null=True)),
                ('post_address', models.TextField(blank=True, null=True)),
                ('next_kin', models.TextField(blank=True, null=True)),
                ('next_kin_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('next_kin_address', models.TextField(blank=True, null=True)),
                ('institution_attended', models.TextField(blank=True, null=True)),
                ('honours', models.TextField(blank=True, null=True)),
                ('transcript', models.TextField(blank=True, null=True)),
                ('transcript_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('year_entry', models.CharField(blank=True, max_length=200, null=True)),
                ('residence', models.CharField(blank=True, choices=[('Residential', 'Residential'), ('Off Campus', 'Off Campus')], max_length=200, null=True)),
                ('nysc', models.TextField(blank=True, null=True)),
                ('nysc_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('appointments', models.TextField(blank=True, null=True)),
                ('publications', models.TextField(blank=True, null=True)),
                ('current_course', models.TextField(blank=True, null=True)),
                ('disability', models.CharField(blank=True, max_length=50, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('objection', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=200, null=True)),
                ('cert1', models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=200, null=True)),
                ('cert1_date', models.CharField(blank=True, max_length=200, null=True)),
                ('cert1_subject', models.TextField(blank=True, null=True)),
                ('cert1_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('cert2', models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("A'Levels", "A'Levels")], max_length=200, null=True)),
                ('cert2_date', models.CharField(blank=True, max_length=200, null=True)),
                ('cert2_subject', models.TextField(blank=True, null=True)),
                ('cert2_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('degree', models.CharField(blank=True, choices=[('IJMB', 'IJMB'), ('JUPEB', 'JUPEB'), ('NCE', 'NCE'), ('ND', 'ND'), ('HND', 'HND')], max_length=200, null=True)),
                ('degree_class', models.CharField(blank=True, max_length=200, null=True)),
                ('degree_img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('jamb_no', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('jamb_score', models.CharField(blank=True, max_length=200, null=True)),
                ('first_choice', models.TextField(blank=True, null=True)),
                ('second_choice', models.TextField(blank=True, null=True)),
                ('extracurricular', models.TextField(blank=True, null=True)),
                ('comp_lit', models.CharField(blank=True, choices=[('Good', 'Good'), ('Fair', 'Fair'), ('No', 'No')], max_length=200, null=True)),
                ('offence', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True)),
                ('offence_detail', models.TextField(blank=True, null=True)),
                ('referee', models.TextField(blank=True, null=True)),
                ('referee_address', models.TextField(blank=True, null=True)),
                ('referee_phone', models.CharField(blank=True, max_length=200, null=True)),
                ('date_applied', models.DateTimeField()),
                ('img', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('pin', models.CharField(blank=True, max_length=200, null=True)),
                ('admitted', models.BooleanField(default=0)),
                ('reason_transfer', models.TextField(blank=True, null=True)),
                ('curr_cgpa', models.TextField(blank=True, null=True)),
                ('curr_uni', models.CharField(blank=True, max_length=256, null=True)),
                ('curr_course', models.CharField(blank=True, max_length=256, null=True)),
                ('curr_year_of_entry', models.CharField(blank=True, max_length=256, null=True)),
                ('email_hod', models.EmailField(blank=True, max_length=255, null=True)),
                ('email_dean', models.EmailField(blank=True, max_length=255, null=True)),
                ('dean_comment', models.TextField(blank=True, null=True)),
                ('hod_comment', models.TextField(blank=True, null=True)),
                ('hod_signature', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('dean_signature', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('choice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='major.Major')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='level.Level')),
                ('session', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=20, unique=True)),
                ('used', models.BooleanField(default=0)),
                ('date_used', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pin_application', to='admission.Application')),
            ],
        ),
    ]
