# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('programme', models.CharField(choices=[('Undergraduate', 'Undergraduate'), ('Postgraduate', 'Postgraduate')], max_length=50)),
                ('programme_type', models.CharField(choices=[('Regular', 'Regular'), ('Transfer', 'Transfer'), ('Direct Entry', 'Direct Entry'), ('Conversion', 'Conversion')], max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=50)),
                ('dateBirth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=20)),
                ('stateOrigin', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=20)),
                ('sponsor', models.CharField(max_length=20)),
                ('sponsor_address', models.TextField()),
                ('sponsor_phone', models.CharField(max_length=20)),
                ('cert', models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("GCE A'Levels", "GCE A'Levels"), ('IJMB', 'IJMB'), ('NCE', 'NCE'), ('ND', 'ND'), ('HND', 'HND')], max_length=20, null=True)),
                ('cert_date', models.CharField(blank=True, max_length=20, null=True)),
                ('degree_class', models.CharField(blank=True, max_length=20, null=True)),
                ('first_choice', models.CharField(max_length=50)),
                ('second_choice', models.CharField(max_length=50)),
                ('extracurricular', models.TextField()),
                ('comp_lit', models.CharField(choices=[('Good', 'Good'), ('Fair', 'Fair'), ('No', 'No')], max_length=10)),
                ('offence', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
                ('offence_detail', models.TextField()),
                ('referee', models.CharField(blank=True, max_length=100, null=True)),
                ('referee_address', models.TextField(blank=True, null=True)),
                ('referee_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('session', models.CharField(max_length=20)),
                ('date_applied', models.DateField()),
                ('admitted', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=20)),
                ('used', models.BooleanField(default=0)),
                ('date_used', models.DateTimeField(blank=True, null=True)),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admission.Application')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('grade', models.CharField(max_length=5)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.Application')),
            ],
        ),
    ]