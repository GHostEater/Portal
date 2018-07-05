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
    q1 = models.IntegerField(default=0)
    q2 = models.IntegerField(default=0)
    q3 = models.IntegerField(default=0)
    q4 = models.IntegerField(default=0)
    q5 = models.IntegerField(default=0)
    q6 = models.IntegerField(default=0)
    q7 = models.IntegerField(default=0)
    q8 = models.IntegerField(default=0)
    q9 = models.IntegerField(default=0)
    q10 = models.IntegerField(default=0)
    q11 = models.IntegerField(default=0)
    q12 = models.IntegerField(default=0)
    q13 = models.IntegerField(default=0)
    q14 = models.IntegerField(default=0)
    q15 = models.IntegerField(default=0)
    q16 = models.IntegerField(default=0)
    q17 = models.IntegerField(default=0)
    q18 = models.IntegerField(default=0)
    q19 = models.IntegerField(default=0)
    q20 = models.IntegerField(default=0)
    q21 = models.IntegerField(default=0)
    q22 = models.IntegerField(default=0)
    q23 = models.IntegerField(default=0)
    q24 = models.IntegerField(default=0)
    q25 = models.IntegerField(default=0)
    q26 = models.IntegerField(default=0)
    q27 = models.IntegerField(default=0)
    q28 = models.IntegerField(default=0)
    q29 = models.IntegerField(default=0)
