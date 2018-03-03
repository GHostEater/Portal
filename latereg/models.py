# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Student, User
from session.models import Session

# Create your models here.


class RegStatus(models.Model):
    duration = models.TextField()
    status = models.IntegerField(default=0)
    date = models.DateTimeField()


class LateReg(models.Model):
    semester_choices = (
        (1, '1st Semester'),
        (2, '2nd Semester'),
    )
    student = models.ForeignKey(Student)
    session = models.ForeignKey(Session)
    semester = models.IntegerField(choices=semester_choices)
    status = models.IntegerField(default=0)


class Log(models.Model):
    student = models.ForeignKey(Student)
    approved_by = models.ForeignKey(User)
    date = models.DateTimeField()
