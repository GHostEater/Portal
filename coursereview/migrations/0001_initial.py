# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-10-08 04:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
        ('accounts', '0001_initial'),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.IntegerField(default=0)),
                ('q2', models.IntegerField(default=0)),
                ('q3', models.IntegerField(default=0)),
                ('q4', models.IntegerField(default=0)),
                ('q5', models.IntegerField(default=0)),
                ('q6', models.IntegerField(default=0)),
                ('q7', models.IntegerField(default=0)),
                ('q8', models.IntegerField(default=0)),
                ('q9', models.IntegerField(default=0)),
                ('q10', models.IntegerField(default=0)),
                ('q11', models.IntegerField(default=0)),
                ('q12', models.IntegerField(default=0)),
                ('q13', models.IntegerField(default=0)),
                ('q14', models.IntegerField(default=0)),
                ('q15', models.IntegerField(default=0)),
                ('q16', models.IntegerField(default=0)),
                ('q17', models.IntegerField(default=0)),
                ('q18', models.IntegerField(default=0)),
                ('q19', models.IntegerField(default=0)),
                ('q20', models.IntegerField(default=0)),
                ('q21', models.IntegerField(default=0)),
                ('q22', models.IntegerField(default=0)),
                ('q23', models.IntegerField(default=0)),
                ('q24', models.IntegerField(default=0)),
                ('q25', models.IntegerField(default=0)),
                ('q26', models.IntegerField(default=0)),
                ('q27', models.IntegerField(default=0)),
                ('q28', models.IntegerField(default=0)),
                ('q29', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
    ]
