# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from course.models import Course
from accounts.models import Student, User
from level.models import Level
from session.models import Session

# Create your models here.


class CourseReg(models.Model):
    class Meta:
        unique_together = ("course", "student", "session")
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    level = models.ForeignKey(Level)
    session = models.ForeignKey(Session)


class ExtraUnitRequest(models.Model):
    student = models.ForeignKey(Student)
    session = models.ForeignKey(Session)
    semester = models.IntegerField()
    status = models.IntegerField()
    units = models.IntegerField()
    date = models.DateTimeField()
    handled_by = models.ForeignKey(User, null=True, blank=True)
