# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from core.models import Course, Major, Level

# Create your models here.


class CourseToMajor(models.Model):
    course = models.ForeignKey(Course)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)


class CourseRegister(models.Model):
    course = models.ForeignKey(Course)
