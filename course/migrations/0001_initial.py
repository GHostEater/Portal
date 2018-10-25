# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('level', '0001_initial'),
        ('dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=10)),
                ('type', models.CharField(choices=[('Compulsory', 'Compulsory'), ('Elective', 'Elective')], max_length=20)),
                ('semester', models.IntegerField(default=0)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Dept')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='level.Level')),
            ],
        ),
    ]