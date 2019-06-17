# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import User, Lecturer
from courseresult.models import CourseResult

# Create your models here.


class Request(models.Model):
    lecturer = models.ForeignKey(Lecturer)
    status = models.IntegerField()
    date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    handled_by = models.ForeignKey(User, null=True, blank=True)

    def __str__(self):
        return str(str(self.lecturer)+" Status:"+str(self.status)+" Start:"+str(self.date)+" End:"+str(self.end_date))


class Log(models.Model):
    result = models.ForeignKey(CourseResult)
    type = models.CharField(max_length=10)
    prev_score = models.FloatField()
    new_score = models.FloatField()
    date = models.DateTimeField()
    edited_by = models.ForeignKey(Lecturer)
