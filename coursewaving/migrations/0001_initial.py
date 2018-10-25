# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20170624_1138'),
        ('course', '0003_auto_20170624_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='WavedCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
                ('wavedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
            ],
        ),
    ]