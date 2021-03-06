# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-07 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='cert',
            new_name='cert1',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='cert_date',
            new_name='cert1_date',
        ),
        migrations.RemoveField(
            model_name='subject',
            name='application',
        ),
        migrations.AddField(
            model_name='application',
            name='cert1_subject',
            field=models.ManyToManyField(blank=True, null=True, related_name='cert1_subject', to='admission.Subject'),
        ),
        migrations.AddField(
            model_name='application',
            name='cert2',
            field=models.CharField(blank=True, choices=[('WAEC', 'WAEC'), ('NECO', 'NECO'), ('NABTEB', 'NABTEB'), ("GCE A'Levels", "GCE A'Levels"), ('IJMB', 'IJMB'), ('NCE', 'NCE'), ('ND', 'ND'), ('HND', 'HND')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='cert2_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='cert2_subject',
            field=models.ManyToManyField(blank=True, null=True, related_name='cert2_subject', to='admission.Subject'),
        ),
        migrations.AlterField(
            model_name='pin',
            name='pin',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
