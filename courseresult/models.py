# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from course.models import Course
from accounts.models import Student
from dept.models import Dept
from level.models import Level
from session.models import Session

# Create your models here.


class CourseResult(models.Model):
    class Meta:
        unique_together = ('course', 'student', 'session')
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    dept = models.ForeignKey(Dept)
    ca = models.FloatField(max_length=5)
    exam = models.FloatField(max_length=5, null=True, blank=True)
    final = models.FloatField(max_length=7, null=True, blank=True)
    grade = models.CharField(max_length=2, null=True, blank=True)
    gp = models.IntegerField(null=True, blank=True)
    rel = models.BooleanField(default=0)
    session = models.ForeignKey(Session)
    level = models.ForeignKey(Level, null=True, blank=True)
    status = models.IntegerField(default=0)


class ReleaseStatus(models.Model):
    status = models.BooleanField(default=False)


class UploadStatus(models.Model):
    ca = models.BooleanField(default=False)
    exam = models.BooleanField(default=False)
