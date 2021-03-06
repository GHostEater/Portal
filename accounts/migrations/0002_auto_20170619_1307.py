# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default='', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dateBirth',
            field=models.DateField(default='1970-01-01', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='genotype',
            field=models.CharField(choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('CS', 'CS')], default='', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.FileField(default='', null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='student',
            name='lga',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nextKin',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nextKinAddress',
            field=models.TextField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='oLevel',
            field=models.CharField(choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('WAEC/GCE', 'WAEC/GCE'), ('NECO/GCE', 'NECO/GCE'), ('WAEC/NECO', 'WAEC/NECO')], default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentNo',
            field=models.CharField(default='', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stateOrigin',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='town',
            field=models.TextField(default='', null=True),
        ),
    ]
