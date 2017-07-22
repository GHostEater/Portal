# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from course.models import Course
from accounts.models import Student
from level.models import Level
from session.models import Session

# Create your models here.


class CourseReg(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    level = models.ForeignKey(Level)
    session = models.ForeignKey(Session)
