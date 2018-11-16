# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-05-04 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_student_parent_email'),
        ('course', '0005_auto_20171002_1433'),
        ('session', '0003_session_is_admission'),
        ('coursereg', '0002_auto_20170708_0827'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coursereg',
            unique_together=set([('course', 'student', 'session')]),
        ),
    ]