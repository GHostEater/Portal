# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from session.models import Session
from accounts.models import Student
from dept.models import Dept

# Create your models here.


class CourseResultGPA(models.Model):
    class Meta:
        unique_together = ('student', 'session', 'semester')

    student = models.ForeignKey(Student)
    session = models.ForeignKey(Session)
    dept = models.ForeignKey(Dept)
    semester = models.IntegerField()
    tcp = models.FloatField()
    tnu = models.FloatField()
    gpa = models.FloatField()
    ctcp = models.FloatField()
    ctnu = models.FloatField()
    cgpa = models.FloatField()
    tce = models.FloatField()
    prev_ctcp = models.FloatField()
    prev_ctnu = models.FloatField()
    prev_cgpa = models.FloatField()
    prev_tce = models.FloatField()
    status = models.IntegerField()
    rel = models.BooleanField(default=0)
