# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-06 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0008_auto_20170906_1344'),
        ('session', '0002_session_actions'),
        ('paymenttype', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=12)),
                ('rrr', models.CharField(max_length=500)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('paymenttype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paymenttype.PaymentType')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Student')),
            ],
        ),
    ]
