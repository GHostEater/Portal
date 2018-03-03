# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from course.models import Course
from accounts.models import Student, Lecturer

# Create your models here.


class WavedCourses(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    waved_by = models.ForeignKey(Lecturer)
