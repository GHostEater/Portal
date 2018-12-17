# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Grade(models.Model):
    grade = models.CharField(max_length=5)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    gp = models.IntegerField()
    active = models.BooleanField(default=True)


class GradePoint(models.Model):
    grade = models.CharField(max_length=255)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    active = models.BooleanField(default=True)
