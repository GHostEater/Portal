# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-04-23 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_student_edit'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='parent_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]
