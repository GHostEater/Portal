# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20170624_1138'),
        ('dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='dept.Dept')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
            ],
        ),
    ]
