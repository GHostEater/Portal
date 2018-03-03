# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import Student, Lecturer
from course.models import Course
from session.models import Session

# Create your models here.


class CourseReview(models.Model):
    student = models.ForeignKey(Student)
    lecturer = models.ForeignKey(Lecturer)
    course = models.ForeignKey(Course)
    session = models.ForeignKey(Session)
    q1 = models.CharField(max_length=256)
    q2 = models.CharField(max_length=256)
    q3 = models.CharField(max_length=256)
    q4 = models.CharField(max_length=256)
    q5 = models.CharField(max_length=256)
    q6 = models.CharField(max_length=256)
    q7 = models.CharField(max_length=256)
    q8 = models.CharField(max_length=256)
    q9 = models.CharField(max_length=256)
    q10 = models.CharField(max_length=256)
