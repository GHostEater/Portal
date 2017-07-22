# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User, Lecturer
from courseResult.models import CourseResult

# Create your models here.


class Request(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    status = models.IntegerField()
    date = models.DateTimeField(null=True)
    handledBy = models.ForeignKey(User, null=True, blank=True)


class Log(models.Model):
    result = models.ForeignKey(CourseResult)
    type = models.CharField(max_length=10)
    prev_score = models.FloatField()
    new_score = models.FloatField()
    date = models.DateTimeField()
    editedBy = models.ForeignKey(Lecturer)
