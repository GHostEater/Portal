# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-18 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20170624_1138'),
        ('courseresult', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10)),
                ('prev_score', models.FloatField()),
                ('new_score', models.FloatField()),
                ('date', models.DateTimeField()),
                ('editedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseresult.CourseResult')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('date', models.DateTimeField(null=True)),
                ('handledBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Lecturer')),
            ],
        ),
    ]
