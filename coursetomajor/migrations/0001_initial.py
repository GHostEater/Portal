# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-08 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('major', '0001_initial'),
        ('level', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseToMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='level.Level')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major')),
            ],
        ),
    ]
