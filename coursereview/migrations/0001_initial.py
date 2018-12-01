# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-12-08 10:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0005_auto_20171002_1433'),
        ('accounts', '0018_auto_20171017_1135'),
        ('session', '0003_session_is_admission'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.CharField(max_length=256)),
                ('q2', models.CharField(max_length=256)),
                ('q3', models.CharField(max_length=256)),
                ('q4', models.CharField(max_length=256)),
                ('q5', models.CharField(max_length=256)),
                ('q6', models.CharField(max_length=256)),
                ('q7', models.CharField(max_length=256)),
                ('q8', models.CharField(max_length=256)),
                ('q9', models.CharField(max_length=256)),
                ('q10', models.CharField(max_length=256)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
    ]
