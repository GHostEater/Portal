# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-24 14:45
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
            name='CourseAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(choices=[(1, '1st Semester'), (2, '2nd Semester')], default=0)),
                ('position', models.IntegerField(choices=[(1, 'Coordinator'), (2, 'Assisting')], default=2)),
                ('allocatedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allocatedBy', to='accounts.Lecturer')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dept.Dept')),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecturer', to='accounts.Lecturer')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='session.Session')),
            ],
        ),
    ]
