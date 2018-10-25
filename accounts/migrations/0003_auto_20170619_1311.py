# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 12:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170619_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeofficer',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college.College'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dept.Dept'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='rank',
            field=models.CharField(blank=True, choices=[('Professor', 'Professor'), ('Associate Professor', 'Associate Professor'), ('Senior Lecturer', 'Senior Lecturer'), ('Lecturer I', 'Lecturer I'), ('Lecturer II', 'Lecturer II'), ('Assistant Lecturer', 'Assistant Lecturer'), ('Graduate Assistant', 'Graduate Assistant')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='status',
            field=models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Adjunct', 'Adjunct')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='bloodGroup',
            field=models.CharField(blank=True, choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='genotype',
            field=models.CharField(blank=True, choices=[('AA', 'AA'), ('AS', 'AS'), ('SS', 'SS'), ('CS', 'CS')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
        migrations.AlterField(
            model_name='student',
            name='lga',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nextKin',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nextKinAddress',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='oLevel',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('WAEC/GCE', 'WAEC/GCE'), ('NECO/GCE', 'NECO/GCE'), ('WAEC/NECO', 'WAEC/NECO')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='parentNo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='religion',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='stateOrigin',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='town',
            field=models.TextField(blank=True, null=True),
        ),
    ]