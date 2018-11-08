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
        ('paymenttype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentToMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jme', models.BooleanField(default=False)),
                ('de', models.BooleanField(default=False)),
                ('conversion', models.BooleanField(default=False)),
                ('pt', models.BooleanField(default=False)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='level.Level')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='major.Major')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymenttype.PaymentType')),
            ],
        ),
    ]
