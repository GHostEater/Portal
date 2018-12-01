# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-08 07:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0006_auto_20170624_1138'),
        ('session', '0001_initial'),
        ('course', '0003_auto_20170624_0927'),
        ('dept', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ca', models.FloatField(max_length=5)),
                ('exam', models.FloatField(blank=True, max_length=5, null=True)),
                ('final', models.FloatField(blank=True, max_length=7, null=True)),
                ('grade', models.CharField(blank=True, max_length=2, null=True)),
                ('gp', models.IntegerField(blank=True, null=True)),
                ('rel', models.BooleanField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Dept')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
    ]
