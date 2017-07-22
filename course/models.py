# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from level.models import Level
from dept.models import Dept

# Create your models here.


class Course(models.Model):
    type_choices = (
        ('Compulsory', 'Compulsory'),
        ('Elective', 'Elective'),
    )
    semester_choices = (
        (1, '1st Semester'),
        (2, '2nd Semester'),
    )
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    type = models.CharField(max_length=20, choices=type_choices)
    ca = models.IntegerField(default=30)
    exam = models.IntegerField(default=70)
    semester = models.IntegerField(choices=semester_choices, default=0)
    level = models.ForeignKey(Level)
    dept = models.ForeignKey(Dept)

    def __str__(self):
        return str(self.code) + ' ' + str(self.title)
